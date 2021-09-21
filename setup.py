#!/usr/bin/python3

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fp:
    longtext = fp.read()

setup(
    name="todo_txt_base",
    version="2.4",
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
                "backuptodo=todo_txt_base.entry_points:backup_todo",
            ],
    },
    setup_requires=["pytest-runner"],
    install_requires=["relatorio", "ConfigArgParse"],
    tests_require=["pytest", "mock"],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
)
