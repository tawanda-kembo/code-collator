from setuptools import setup, find_packages
import pathlib
import os

here = pathlib.Path(__file__).parent.resolve()


def get_version():
    version = os.environ.get('PACKAGE_VERSION', '0.0.0')
    return version


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
    packages=find_packages(include=['code_collator', 'code_collator.*']),
    python_requires=">=3.6, <4",
    install_requires=[
        'pygments',
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
