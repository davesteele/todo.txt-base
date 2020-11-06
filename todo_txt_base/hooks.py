# Copyright (c) 2020 David Steele <dsteele@gmail.com>
#
# SPDX-License-Identifier: GPL-2.0-or-later
# License-Filename: LICENSE

from functools import wraps
from pathlib import Path
from subprocess import run

PRE_HOOK_DIR = "/etc/todo.txt-base/prehooks"
POST_HOOK_DIR = "/etc/todo.txt-base/posthooks"


def run_hooks(dir):
    print("Running hooks on %s" % dir)
    dir_path = Path(dir)

    script_paths = [x for x in dir_path.iterdir() if x.is_file]

    scripts = sorted([str(x) for x in script_paths])

    for script in scripts:
        print(script)
        run([script])


def prehook(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        run_hooks(PRE_HOOK_DIR)
        return fn(*args, **kwargs)

    return fn


def posthook(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        returnval = fn(*args, **kwargs)
        run_hooks(POST_HOOK_DIR)
        return returnval

    return fn
