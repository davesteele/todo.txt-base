% todo.txt-base(5)
%
% November 2020

# NAME

todo.txt-base -- Common support for todo.txt packages

## DESCRIPTION

The todo.txt-base package contains utility functions supporting packages that
provide the virtual todo.txt package. Users should not install this package
directly.

Hooks are provided that can be run before and after todo.txt file processing.
Scripts run before processing are to be stored in
_/etc/todo.txt-base/prehooks_. Scripts run after processing are stored in
_/etc/todo.txt-base/posthooks_. All scripts are run with a single argument
defining the location of the todo.txt tasking file.

The todo.txt utility _todo.txt-helper_ is used to determine the location of the
todo.txt tasking file.

## SEE ALSO
todo.txt-base(8), vitodo(8), edittodo(8), listtodo(8), todo.txt(8), todo.txt-helper(8)
