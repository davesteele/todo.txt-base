#!/usr/bin/python3
# Copyright (c) 2020 David Steele <dsteele@gmail.com>
#
# SPDX-License-Identifier: GPL-2.0-or-later
# License-Filename: LICENSE


import sys
from pathlib import Path
from subprocess import run

import todo_txt_base.tdtlist as tdtlist
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

    # TODO - temp
    # this is a temp kluge to bridge from v1.1 to v2.0
    if phase == "ls":
        print("running kluge")
        cp = run("cd /tmp; /usr/bin/topydo ls", shell=True, capture_output=True, encoding="utf-8")
        print(cp.stdout)


@tdtwrapper
@prehook
def list_todo(exe_path, task_path):
    sys.argv = ["listtodo", "-f", task_path] + sys.argv[1:]
    tdtlist.main()
