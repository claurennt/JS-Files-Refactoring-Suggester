import os
from ollama import Client
from dotenv import load_dotenv

from find_files import find_files_in_dir

load_dotenv()


def refactor_code(code: str):
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
    for part in client.chat("gpt-oss:120b", messages=messages, stream=True):
        print(part.message.content, end="", flush=True)


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
    foundFiles = find_files_in_dir(
        args.path, file_extensions=exts, ignored_directories=ignored_dirs
    )
    print(foundFiles)
    for i in range(len(foundFiles)):
        if i == 0:
            with open(foundFiles[i]) as f:
                code = f.read()
                refactor_code(code)
