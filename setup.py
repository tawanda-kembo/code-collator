from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
    name="code-collator",
    version="0.1",
    description="A CLI tool to aggregate codebase into a single Markdown file",
    long_description=(here / 'README.md').read_text(encoding='utf-8'),
    long_description_content_type='text/markdown',
    url="https://github.com/tawanda-kembo/code-collator",
    author="Tawanda Kembo",
    author_email="tkembo@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="cli, development, documentation",
    packages=find_packages(),
    python_requires=">=3.6, <4",
    install_requires=[
        # Add any dependencies here
    ],
    entry_points={
        "console_scripts": [
            "code-collator=code_collator.collate:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/tawanda-kembo/code-collator/issues",
        "Source": "https://github.com/tawanda-kembo/code-collator",
    },
)