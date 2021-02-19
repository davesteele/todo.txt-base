# Copyright (c) 2020 David Steele <dsteele@gmail.com>
#
# SPDX-License-Identifier: GPL-2.0-or-later
# License-Filename: LICENSE

import sys
from functools import wraps
from pathlib import Path
from subprocess import run

from todo_txt_base.tconfig import get_var, TDTBaseException

PRE_HOOK_DIR = "/etc/todo.txt-base/prehooks"
POST_HOOK_DIR = "/etc/todo.txt-base/posthooks"


def run_hooks(dir, task_path):
    dir_path = Path(dir)

    script_paths = [x for x in dir_path.iterdir() if x.is_file]

    scripts = sorted([str(x) for x in script_paths])

    for script in scripts:
        run([script, task_path])


def prehook(fn):
    @wraps(fn)
    def wrapper(exe_path, task_path, *args, **kwargs):
        run_hooks(PRE_HOOK_DIR, task_path)
        return fn(exe_path, task_path, *args, **kwargs)

    return wrapper


def posthook(fn):
    @wraps(fn)
    def wrapper(exe_path, task_path, *args, **kwargs):
        returnval = fn(exe_path, task_path, *args, **kwargs)
        run_hooks(POST_HOOK_DIR, task_path)
        return returnval

    return wrapper


def tdtwrapper(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            task_path = get_var("task_path")
            exe_path = get_var("executable")
            return fn(exe_path, task_path, *args, **kwargs)
        except TDTBaseException:
            sys.exit(1)

    return wrapper
