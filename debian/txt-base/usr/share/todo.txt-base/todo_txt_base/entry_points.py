#!/usr/bin/python3
# Copyright (c) 2020 David Steele <dsteele@gmail.com>
#
# SPDX-License-Identifier: GPL-2.0-or-later
# License-Filename: LICENSE


import sys
from subprocess import run

import tdtlist
from hooks import posthook, prehook


def run_todo(app):
    cmd = [app] + sys.argv[1:]
    run(cmd)


@prehook
@posthook
def vi_todo():
    run_todo("vi")


@prehook
@posthook
def edit_todo():
    run_todo("editor")


@prehook
@posthook
def execute_todo():
    run_todo("todo.txt")


def list_todo():
    tdtlist.main()


def main():
    print("Hello World")
    print(sys.argv)


main()
