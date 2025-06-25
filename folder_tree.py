"""
Folder Tree CLI Tool
A command-line utility to generate tree structure of directories and files.
"""

import os
import argparse
from pathlib import Path
from typing import List, Tuple, Set

class TreeGenerator:
    def __init__(self, show_files: bool = True, max_depth: int = None, include_hidden: bool = False, ignore_list: str = ""):
        self.show_files = show_files
        self.max_depth = max_depth
        self.include_hidden = include_hidden
        self.ignored_folders, self.ignored_files = self._parse_ignore_list(ignore_list)
        
    def _parse_ignore_list(self, ignore_list: str) -> Tuple[Set[str], Set[str]]:
        """Parse the comma-separated ignore list into folders and files."""
        if not ignore_list:
            return set(), set()
        
        items = ignore_list.split(',')
        folders = set()
        files = set()
        
        for item in items:
            item = item.strip()
            if item.startswith('/'):
                folders.add(item[1:])
            else:
                files.add(item)
        
        return folders, files
    
    def _should_ignore_item(self, item: Path) -> bool:
        """Check if an item should be ignored based on the ignore list."""
        item_name = item.name
        
        if item.is_dir():
            return item_name in self.ignored_folders
        else:
            return item_name in self.ignored_files
        
    def generate_tree(self, root_path: str) -> str:
        """Generate tree structure for the given root path."""
        root = Path(root_path)
        
        if not root.exists():
            return f"Error: Path '{root_path}' does not exist."
        
        if not root.is_dir():
            return f"Error: '{root_path}' is not a directory."
        
        tree_lines = [str(root)]
        self._build_tree(root, "", tree_lines, 0)
        return "\n".join(tree_lines)
    
    def _build_tree(self, path: Path, prefix: str, tree_lines: List[str], depth: int):
        """Recursively build the tree structure."""
        if self.max_depth is not None and depth >= self.max_depth:
            return
        
        try:
            # All items in the directory
            items = list(path.iterdir())
            
            # Filter items based on show_files is True or False
            if self.show_files:
                dirs = [item for item in items if item.is_dir()]
                files = [item for item in items if item.is_file()]
                all_items = sorted(dirs) + sorted(files)
            else:
                all_items = sorted([item for item in items if item.is_dir()])
            
            # Skip hidden files/folders unless include_hidden is True
            if not self.include_hidden:
                all_items = [item for item in all_items if not item.name.startswith('.')]
            
            # Filter out ignored items
            all_items = [item for item in all_items if not self._should_ignore_item(item)]
            
            # Create the Folder Tree
            for i, item in enumerate(all_items):
                is_last = i == len(all_items) - 1
                
                if is_last:
                    current_prefix = "└── "
                    next_prefix = prefix + "    "
                else:
                    current_prefix = "├── "
                    next_prefix = prefix + "│   "
                
                item_name = item.name
                if item.is_dir():
                    item_name += "/"
                
                tree_lines.append(f"{prefix}{current_prefix}{item_name}")
                
                # Recursively process subdirectories
                if item.is_dir():
                    self._build_tree(item, next_prefix, tree_lines, depth + 1)
                    
        except PermissionError:
            tree_lines.append(f"{prefix}├── [Permission Denied]")


def main():
    parser = argparse.ArgumentParser(
        description="Generate a tree structure of directories and files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python tree_cli.py /path/to/folder
    python tree_cli.py /path/to/folder --folders-only
    python tree_cli.py /path/to/folder --max-depth 2
    python tree_cli.py . --folders-only --max-depth 3
    python tree_cli.py /path/to/folder --ignore "/node_modules,/dist,.env,package-lock.json"
    python tree_cli.py . --ignore "/build,/target,*.log,temp.txt"
        """
    )
    
    parser.add_argument(
        "path",
        help="Path to the directory to generate tree for"
    )
    
    parser.add_argument(
        "--folders-only", "-f",
        action="store_true",
        help="Show only folders, exclude files"
    )
    
    parser.add_argument(
        "--max-depth", "-d",
        type=int,
        help="Maximum depth to traverse (default: unlimited)"
    )
    
    parser.add_argument(
        "--include-hidden", "-i",
        action="store_true",
        help="Include hidden files and folders (starting with .)"
    )
    
    parser.add_argument(
        "--ignore", "-g",
        type=str,
        default="",
        help="Comma-separated list of folders (with /) and files to ignore (e.g., '/node_modules,/dist,.env,package.json')"
    )
    
    args = parser.parse_args()
    
    tree_gen = TreeGenerator(
        show_files=not args.folders_only,
        max_depth=args.max_depth,
        include_hidden=args.include_hidden,
        ignore_list=args.ignore
    )
    
    tree_output = tree_gen.generate_tree(args.path)
    print(tree_output)


if __name__ == "__main__":
    main()