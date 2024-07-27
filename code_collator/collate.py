import os
import argparse
from pathlib import Path
import logging

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
            for byte in f.read():
                if byte > 127:
                    return True
    except Exception as e:
        logging.error(f"Error reading file {filepath}: {e}")
        return False
    return False

def read_gitignore(path):
    """Read the .gitignore file and return patterns to ignore."""
    gitignore_path = os.path.join(path, '.gitignore')
    if not os.path.exists(gitignore_path):
        return []
    
    try:
        with open(gitignore_path, 'r') as f:
            patterns = f.read().splitlines()
        logging.info(f"Loaded .gitignore patterns from {gitignore_path}")
        return patterns
    except Exception as e:
        logging.error(f"Error reading .gitignore file {gitignore_path}: {e}")
        return []

def should_ignore(file_path, ignore_patterns):
    """Check if a file should be ignored based on .gitignore patterns and if it's in the .git directory."""
    from fnmatch import fnmatch
    if '.git' in Path(file_path).parts:
        return True
    for pattern in ignore_patterns:
        if fnmatch(file_path, pattern):
            return True
    return False

def collate_codebase(path, output_file):
    """Aggregate the codebase into a single Markdown file."""
    ignore_patterns = read_gitignore(path)
    try:
        with open(output_file, 'w') as output:
            output.write("# Collated Codebase\n\n")
            for root, _, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if should_ignore(file_path, ignore_patterns):
                        logging.info(f"Ignored file {file_path}")
                        continue
                    
                    output.write(f"## {file_path}\n\n")
                    if is_binary_file(file_path):
                        output.write(f"**Note**: This is a binary file.\n\n")
                    elif file.endswith('.svg'):
                        output.write(f"**Note**: This is an SVG file.\n\n")
                    else:
                        try:
                            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                content = f.read()
                                output.write(f"```\n{content}\n```\n\n")
                        except Exception as e:
                            logging.error(f"Error reading file {file_path}: {e}")
                            output.write(f"**Note**: Error reading this file.\n\n")
        logging.info(f"Collated codebase written to {output_file}")
    except Exception as e:
        logging.error(f"Error writing to output file {output_file}: {e}")

def main():
    """Parse arguments and initiate codebase collation."""
    setup_logging()
    parser = argparse.ArgumentParser(description="Aggregate codebase into a single Markdown file.")
    parser.add_argument('-p', '--path', type=str, default='.', help="Specify the path to the codebase directory (default: current directory)")
    parser.add_argument('-o', '--output', type=str, default='collated-code.md', help="Specify output file (default: collated-code.md)")
    
    args = parser.parse_args()
    
    logging.info(f"Starting code collation for directory: {args.path}")
    collate_codebase(args.path, args.output)
    logging.info("Code collation completed.")

if __name__ == "__main__":
    main()