# Copyright (c) 2020 David Steele <dsteele@gmail.com>
#
# SPDX-License-Identifier: GPL-2.0-or-later
# License-Filename: LICENSE

import os
from contextlib import contextmanager
from functools import wraps


def none_on_exception(*exceptions):
    def _none_on_exception(fp):
        @wraps(fp)
        def wrapper(*args, **kwargs):
            try:
                return fp(*args, **kwargs)
            except exceptions:
                return None

        return wrapper

    return _none_on_exception


@contextmanager
def nullfd(fd):
    saveout = os.dup(fd)
    os.close(fd)
    os.open(os.devnull, os.O_RDWR)
    try:
        yield
    finally:
        os.dup2(saveout, fd)
        os.close(saveout)
