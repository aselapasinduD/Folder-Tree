# Folder Tree CLI Tool

A lightweight and flexible command-line utility to generate visual tree structures of directories and files. Perfect for documentation, project exploration, and understanding folder hierarchies.

### Features

-   🌳 **Visual Tree Structure**: Generate clean, ASCII-based tree representations.
-   🔍 **Depth Control**: Limit traversal depth to focus on specific levels.
-   🙈 **Hidden Files Support**: Include or exclude hidden files and folders.
-   🚫 **Smart Filtering**: Ignore specific files and folders with pattern matching.
-   🛡️ **Permission Handling**: Gracefully handles permission-denied scenarios.

### Command Line Options
|Option|Short|Description|
|--|--|--|
|`--folders-only`|`-f`|Show only folders, exclude files|
|`--max-depth`|`-d`|Maximum depth to traverse|
|`--include-hidden`|`-i`|Include hidden files and folders (starting with .)|
|`--ignore`|`-g`|Comma-separated list of items to ignore|

## Example
bash
```bash
folder_tree /full/path/to/project --ignore "/build"
```
> **Note:**  You can run `folder_tree` command from the console anyware in windows after you add the folder path containing `folder_tree.exe` to your **Windows Environment Variables**.

OR
```bash
folder_tree.exe /full/path/to/project --ignore "/build"
```
> **Note:** Only work when you open the console on same folder that containing the `folder_tree.exe` file.

Folder structure of the source files after building the executable file.
```bsh
├── assets/
│   ├── folder-tree-100-icon.ico
│   ├── folder-tree-100-icon.png
│   └── folder-tree-100-icon.psd
├── dist/
│   └── folder_tree.exe
├── folder_tree.py
├── folder_tree.spec
└── README.md
```

# How to Use It

## Regular Use

You can use the executable file from the **v0.1.0 release**.

#### Step 1: Download the Executable
- Download the `folder_tree.exe` file from the release.

> **Note:** You can run `folder_tree.exe` from the console in Windows by opening the folder location in the terminal.

#### Step 2: Set Environment Variable
- Add the folder path containing `folder_tree.exe` to your **Windows Environment Variables**.

Now you're ready to use the tool from anywhere in your console!

## Developer Use

## Installation

1. Clone this repository.
2. Ensure you have Python 3.6+ installed.
3. The tool uses only the Python standard library; no additional dependencies are required!

## Usage.

### Basic Usage

Generate a tree for the **current directory**:

```bash
python tree_cli.py .
```

Generate a tree for a **specific path**:

```bash
python tree_cli.py /path/to/your/folder
```

## Ignore Patterns

The `--ignore` option supports two types of patterns:

-   **Folders**: Prefix with `/` (e.g., `/node_modules`, `/dist`)
-   **Files**: No prefix needed (e.g., `.env`, `package-lock.json`, `*.log`)

### Common Ignore Patterns

**For Node.js projects:**

```bash
--ignore "/node_modules,/dist,/.next,package-lock.json,.env"
```

**For Python projects:**

```bash
--ignore "/__pycache__,/.venv,.env"
```

**For Java projects:**

```bash
--ignore "/target,/build,.gradle"
```

## Sample Output

```
/home/user/my-project
├── src/
│   ├── components/
│   │   ├── Header.tsx
│   │   └── Footer.tsx
│   ├── utils/
│   │   └── helpers.py
│   └── main.py
├── tests/
│   └── test_main.py
├── README.md
└── package.json
```
## Support

If you encounter any issues or have questions:

1.  Check the [Issues](../../issues) page for existing solutions
2.  Create a new issue with detailed information
3.  Include your Python version and operating system

Made with ❤️ for developers who love clean, organized code structures.