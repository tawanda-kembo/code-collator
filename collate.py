from pygments import lexers, token
from pygments.util import ClassNotFound
import logging

def process_file_content(content, file_path, include_comments):
    """Process file content, optionally removing comments and docstrings."""
    if include_comments:
        return content

    try:
        lexer = lexers.get_lexer_for_filename(file_path)
    except ClassNotFound:
        logging.warning(f"No lexer found for {file_path}. Returning original content.")
        return content

    tokens = list(lexer.get_tokens(content))
    processed_tokens = [
        (token_type, value) for token_type, value in tokens
        if token_type not in (token.Comment, token.Comment.Single, token.Comment.Multiline, token.String.Doc)
    ]

    return ''.join(value for _, value in processed_tokens)
