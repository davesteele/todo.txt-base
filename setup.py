#!/usr/bin/python3

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fp:
    longtext = fp.read()

setup(
    name="todo_txt_base",
    version="1.0",
    description="foo",
    url="https://example.com",
    author="David Steele",
    author_email="steele@debian.org",
    packages=find_packages(),
    long_description=longtext,
    long_description_content_type="text/markdown",
    package_data={"": ["*.odt"]},
    entry_points={
        "console_scripts": [
                "todo.txt-base=todo_txt_base.entry_points:execute_todo",
                "vitodo=todo_txt_base.entry_points:vi_todo",
                "edittodo=todo_txt_base.entry_points:edit_todo",
                "listtodo=todo_txt_base.entry_points:list_todo",
            ],
    },
    install_requires=["relatorio"],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
)