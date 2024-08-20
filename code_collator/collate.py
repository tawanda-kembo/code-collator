import os
import argparse
from pathlib import Path
import logging
from fnmatch import fnmatch


def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


def is_binary_file(filepath):
    """Check if a file is binary."""
    try:
        with open(filepath, 'rb') as f:
            chunk = f.read(1024)
            return b'\x00' in chunk
    except Exception as e:
        logging.error("Error reading file %s: %s", filepath, e)
        return False


def read_gitignore(path):
    """Read the .gitignore file and return patterns to ignore."""
    gitignore_path = os.path.join(path, '.gitignore')
    if not os.path.exists(gitignore_path):
        return []

    try:
        with open(gitignore_path, 'r') as f:
            patterns = f.read().splitlines()
        logging.info("Loaded .gitignore patterns from {gitignore_path}")
        return patterns
    except Exception as e:
        logging.error(f"Error reading .gitignore file {gitignore_path}: {e}")
        return []


def should_ignore(file_path, ignore_patterns):
    """Check if a file should be ignored based on .gitignore patterns and if it's in the .git directory."""
    if '.git' in Path(file_path).parts:
        return True

    relative_path = os.path.relpath(file_path)
    path_parts = relative_path.split(os.sep)

    for pattern in ignore_patterns:
        if pattern.endswith('/'):
            # Directory pattern
            if any(fnmatch(part, pattern[:-1]) for part in path_parts):
                return True
        elif '/' in pattern:
            # Path pattern
            if fnmatch(relative_path, pattern):
                return True
        else:
            # File pattern
            if fnmatch(os.path.basename(file_path), pattern):
                return True

    return False


def collate_codebase(path, output_file):
    """Aggregate the codebase into a single Markdown file."""
    ignore_patterns = read_gitignore(path)
    try:
        with open(output_file, 'w', encoding='utf-8') as output:
            output.write("# Collated Codebase\n\n")
            for root, _, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if should_ignore(file_path, ignore_patterns):
                        logging.info("Ignored file %s", file_path)
                        continue

                    output.write(f"## {file_path}\n\n")
                    is_binary = is_binary_file(file_path)
                    logging.info("File %s is binary: %s", file_path, is_binary)
                    if is_binary:
                        output.write("**Note**: This is a binary file.\n\n")
                    elif file.endswith('.svg'):
                        output.write("**Note**: This is an SVG file.\n\n")
                    else:
                        try:
                            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                content = f.read()
                                output.write(f"```\n{content}\n```\n\n")
                        except Exception as e:
                            logging.error("Error reading file %s: %s", file_path, e)
                            output.write("**Note**: Error reading this file.\n\n")
        logging.info("Collated codebase written to %s", output_file)
    except Exception as e:
        logging.error("Error writing to output file %s: %s", output_file, e)


def main():
    """Parse arguments and initiate codebase collation."""
    setup_logging()
    parser = argparse.ArgumentParser(description="Aggregate codebase into a single Markdown file.")
    parser.add_argument(
        '-p',
        '--path',
        type=str,
        default='.',
        help="Specify the path to the codebase directory (default: current directory)")
    parser.add_argument('-o', '--output', type=str, default='collated-code.md',
                        help="Specify output file (default: collated-code.md)")

    args = parser.parse_args()

    logging.info("Starting code collation for directory: %s", args.path)
    collate_codebase(args.path, args.output)
    logging.info("Code collation completed.")


if __name__ == "__main__":
    main()
