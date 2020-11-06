#!/usr/bin/python3
# Copyright (c) 2020 David Steele <dsteele@gmail.com>
#
# SPDX-License-Identifier: GPL-2.0-or-later
# License-Filename: LICENSE


import sys
from pathlib import Path
from subprocess import run, PIPE

import todo_txt_base.tdtlist as tdtlist
from todo_txt_base.hooks import posthook, prehook


def run_todo(argarray):
    run(argarray)

def get_todo_path():
    cp = run(
        "todo.txt-helper todofile".split(),
        encoding="utf-8",
        stdout=PIPE,
    )
    path = Path(cp.stdout.strip())
    return str(path.expanduser())


@prehook
@posthook
def vi_todo():
    todo_path = get_todo_path()
    run_todo(["vi", todo_path])


@prehook
@posthook
def edit_todo():
    todo_path = get_todo_path()
    run_todo(["editor", todo_path])


@prehook
@posthook
def execute_todo():
    run_todo(["todo.txt"] + sys.argv[1:])


def list_todo():
    todo_path = get_todo_path()
    sys.argv = ["listtodo", "-f", todo_path] + sys.argv[1:]
    tdtlist.main()


def main():
    print("Hello World")
    print(get_todo_path())
    print(sys.argv)
