# React Files Refactoring Suggester 🐍⚛️

A learning project in Python to analyze React components and suggest refactoring improvements

## About This Project

As I learn Python, I'm building this tool to:

- Practice Python programming concepts

- Create something practical for my React development workflow

- Learn about code analysis and refactoring patterns

- Understand how to build CLI tools in Python

### Project Goals

| Goal                                       | Status      |
| ------------------------------------------ | ----------- |
| Find react files in a project              | Done        |
| Analyze React components for common issues | In Progress |
| Suggest specific refactoring improvements  | Planned     |
| Generate refactoring reports               | Planned     |
| Create IDE/Editor extensions               | Future      |

### Features

<span aria-hidden>🔍</span> Recursive Search: Searches through directories and subdirectories

<span aria-hidden>🚫</span> Smart Ignoring: Automatically skips ignored directories (like node_modules, **tests**, etc.)

<span aria-hidden>⚙️</span> Customizable: Configure file extensions and ignored directories via command line

<span aria-hidden>📁</span> Hidden Directory Protection: Automatically skips directories starting with . (like .git, .vscode)

## Installation

No installation required! Just make sure you have Python 3+ installed.

## Usage

### Basic Usage

Find all .tsx and .jsx files in the current directory:

```bash
python find_files.py
```

### Find Files in Specific Directory

```bash
python find_files.py /path/to/your/project
Custom File Extensions
```

### Find only .js files:

```bash
python find_files.py -e .js
```

### Find multiple extensions:

```bash
python find_files.py -e .js .jsx .ts .tsx
```

### Custom Ignored Directories

```bash
python find_files.py -ignored .git node_modules coverage
```

### Full Example

```bash
python find_files.py /my/react/project -e .tsx .ts -ignored node_modules dist .git
Command Line Arguments
Argument Short Description Default
path - Directory to scan (optional) Current directory (.)
--extensions -e File extensions to include .tsx .jsx
--ignored_directories -ignored Directories to ignore node_modules **tests** dist build
```

#### Command Line Arguments

| Argument              | Short    | Description                | Default                      |
| --------------------- | -------- | -------------------------- | ---------------------------- |
| path                  |          | Current directory (.)      | Directory to scan (optional) |
| --extensions          | -e       | File extensions to include | .tsx .jsx                    |
| --ignored_directories | -ignored | Directories to ignore      | node_modules **tests** dist  |

##### Example Output

```text
Found 24 react files in /Users/username/projects/my-app
./src/components/Button.tsx
./src/components/Header.jsx
./src/pages/Home.tsx
./src/pages/About.jsx
```
