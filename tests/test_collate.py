import sys
import os
import pytest
import logging
from unittest.mock import mock_open, patch

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from code_collator import collate
import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_is_binary_file():
    with patch('builtins.open', mock_open(read_data=b'\x00binary\xff')):
        assert collate.is_binary_file('test.bin') is True

    with patch('builtins.open', mock_open(read_data=b'hello world')):
        assert collate.is_binary_file('test.txt') is False


def test_read_gitignore():
    with patch('builtins.open', mock_open(read_data='*.pyc\n__pycache__\n')):
        patterns = collate.read_gitignore('.')
        assert patterns == ['*.pyc', '__pycache__']


def test_should_ignore():
    patterns = ['*.pyc', '__pycache__']
    assert collate.should_ignore('test.pyc', patterns)
    assert collate.should_ignore('test.py', patterns) is False
    assert collate.should_ignore('.git/config', patterns)


def test_process_file_content():
    content = '''
def hello():
    """This is a docstring."""
    # This is a comment
    print("Hello, World!")
'''
    file_path = "test.py"

    # Test with comments included
    processed = collate.process_file_content(content, file_path, include_comments=True)
    assert '"""This is a docstring."""' in processed
    assert '# This is a comment' in processed

    # Test with comments excluded
    processed = collate.process_file_content(content, file_path, include_comments=False)
    assert '"""This is a docstring."""' not in processed
    assert '# This is a comment' not in processed
    assert 'print("Hello, World!")' in processed


@pytest.fixture
def mock_file_system(tmp_path):
    d = tmp_path / "test_dir"
    d.mkdir()
    (d / "test.py").write_text("# This is a comment\nprint('hello')")
    (d / "test.pyc").write_bytes(b'\x00\x01\x02')
    return d


def test_collate_codebase(mock_file_system, caplog):
    caplog.set_level(logging.INFO)
    output_file = mock_file_system / "output.md"

    # Test with comments included
    collate.collate_codebase(str(mock_file_system), str(output_file), include_comments=True)
    with open(output_file, 'r') as f:
        content = f.read()
    assert "# Collated Codebase" in content
    assert "test.py" in content
    assert "print('hello')" in content
    assert "# This is a comment" in content

    # Test with comments excluded
    collate.collate_codebase(str(mock_file_system), str(output_file), include_comments=False)
    with open(output_file, 'r') as f:
        content = f.read()
    assert "# Collated Codebase" in content
    assert "test.py" in content
    assert "print('hello')" in content
    assert "# This is a comment" not in content


def test_main(mock_file_system, caplog, capsys):
    caplog.set_level(logging.INFO)

    # Test with comments included
    output_with_comments = mock_file_system / 'output_with_comments.md'
    with patch('sys.argv', ['collate', '-p', str(mock_file_system), '-o', str(output_with_comments), '-c', 'on']):
        collate.main()

    with open(output_with_comments, 'r') as f:
        content = f.read()
    assert "# This is a comment" in content

    # Test with comments excluded
    output_without_comments = mock_file_system / 'output_without_comments.md'
    with patch('sys.argv', ['collate', '-p', str(mock_file_system), '-o', str(output_without_comments), '-c', 'off']):
        collate.main()

    with open(output_without_comments, 'r') as f:
        content = f.read()
    assert "# This is a comment" not in content

    # Assert log messages
    assert "Starting code collation for directory:" in caplog.text
    assert "Code collation completed." in caplog.text

    # Check if specific files were processed
    assert f"File {mock_file_system}/test.py is binary: False" in caplog.text
    assert f"File {mock_file_system}/test.pyc is binary: True" in caplog.text
