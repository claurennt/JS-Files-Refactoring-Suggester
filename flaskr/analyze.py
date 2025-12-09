import os
from ollama import Client
from dotenv import load_dotenv


load_dotenv()


def analyze(code: str):
    client = Client(
        host="https://ollama.com",
        headers={"Authorization": "Bearer " + os.environ.get("OLLAMA_API_KEY")},
    )

    messages = [
        {
            "role": "user",
            "content": f"refactor the code from the following file to improve its performance and readability:\n\n{code}",
        },
    ]

    AI_response = ""

    try:
        # Get streaming response
        stream = client.chat(model="gpt-oss:120b", messages=messages, stream=True)

        for chunk in stream:
            # Handle different response formats
            if hasattr(chunk, "message") and chunk.message:
                if hasattr(chunk.message, "content"):
                    AI_response += chunk.message.content
            elif hasattr(chunk, "content"):
                AI_response += chunk.content
            elif isinstance(chunk, dict):
                if "message" in chunk and "content" in chunk["message"]:
                    AI_response += chunk["message"]["content"]
                elif "content" in chunk:
                    AI_response += chunk["content"]
            elif isinstance(chunk, str):
                AI_response += chunk
        print(AI_response)
        return AI_response

    except Exception as e:
        return f"Error calling Ollama API: {str(e)}"


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog="File refactor",
        description="Suggest code refactor using Ollama API",
    )
    parser.add_argument("path", nargs="?", default=".", help="Directory to scan")
    parser.add_argument(
        "-e",
        "--extensions",
        nargs="+",
        default=[".tsx", ".jsx"],
        help="File extensions to include (e.g. .tsx .jsx)",
    )
    parser.add_argument(
        "-ignored",
        "--ignored_directories",
        nargs="+",
        default=["node_modules", "__tests__", "dist", "build"],
        help="Directories to ignore (e.g. .git node_modules)",
    )

    args = parser.parse_args()
    exts = tuple(args.extensions)
    ignored_dirs = tuple(args.ignored_directories)

    from flaskr.find_files import find_files_in_dir

    found_files = find_files_in_dir(
        args.path, file_extensions=exts, ignored_directories=ignored_dirs
    )

    found_files = dict(enumerate(found_files, 1))
    length = len(found_files)
    print(f"Found {length} JS files")
    for key, value in found_files.items():
        print(f"{key}: {value}")

    user_choice = input(
        f">>>> Which file would you like to analyze with AI? Chose one between 1 and {length}:\n"
    )
    chosen_file = found_files[int(user_choice)]

    content = ""

    with open(chosen_file, "r") as f:
        content = f.read()

    analyze(content)
