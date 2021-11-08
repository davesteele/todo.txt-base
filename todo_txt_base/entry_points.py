#!/usr/bin/python3
# Copyright (c) 2020 David Steele <dsteele@gmail.com>
#
# SPDX-License-Identifier: GPL-2.0-or-later
# License-Filename: LICENSE


import os
import sys
from pathlib import Path
from subprocess import run

import todo_txt_base.tdtlist as tdtlist
import todo_txt_base.tdtbackup as tdtbackup
from todo_txt_base.hooks import posthook, prehook, tdtwrapper, run_hooks


@tdtwrapper
@prehook
@posthook
def vi_todo(exe_path, task_path):
    run(["vi", task_path])


@tdtwrapper
@prehook
@posthook
def edit_todo(exe_path, task_path):
    run(["editor", task_path])


@tdtwrapper
def execute_todo(exe_path, task_path):
    phase = sys.argv[1]
    if phase in ["pre", "post"]:
        textfile = sys.argv[2]
        dir = Path("/etc/todo.txt-base/{}hooks/".format(phase))
        run_hooks(str(dir), task_path)


@tdtwrapper
@prehook
def list_todo(exe_path, task_path):
    sys.argv = ["listtodo", "-f", task_path] + sys.argv[1:]
    tdtlist.main()


@tdtwrapper
def backup_todo(exe_path, task_path):
    backup_path = Path(task_path).parent / "backup"
    sys.argv = ["backuptodo", "-f", task_path, "-b", str(backup_path)] + sys.argv[1:]
    tdtbackup.main()


@tdtwrapper
def cd_todo(exe_path, task_path):
    task_dir_path = Path(task_path).parent
    shell_path = os.getenv("SHELL")
    os.chdir(str(task_dir_path))
    run(shell_path)
