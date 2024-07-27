from setuptools import setup, find_packages
import pathlib
import subprocess

here = pathlib.Path(__file__).parent.resolve()

def get_version():
    try:
        version = subprocess.check_output(['git', 'describe', '--tags', '--always']).decode().strip()
        return version.lstrip('v')
    except subprocess.CalledProcessError:
        return '0.0.0'

setup(
    name="code-collator",
    version=get_version(),
    description="A CLI tool to aggregate codebase into a single Markdown file",
    long_description=(here / 'README.md').read_text(encoding='utf-8'),
    long_description_content_type='text/markdown',
    url="https://github.com/tawanda-kembo/code-collator",
    author="Tawanda Kembo",
    author_email="tawanda@mrkembo.com",
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