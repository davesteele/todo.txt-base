% edittodo(8)
%
% November 2020

# NAME

edittodo -- Edit the configured todo.txt tasking file using the default editor

## SYNOPSIS

`edittodo`

## DESCRIPTION

This command opens the configured todo.txt tasking file using the default
editor.

Hooks are provided that can be run before and after todo.txt file processing.
Scripts run before processing are to be stored in
_/etc/todo.txt-base/prehooks_. Scripts run after processing are stored in
_/etc/todo.txt-base/posthooks_. All scripts are run with a single argument
defining the location of the todo.txt tasking file.

The todo.txt utility _todo.txt-helper_ is used to determine the location of the
todo.txt tasking file.

## SEE ALSO
todo.txt-base(8), todo(8), edittodo(8), listtodo(8), todo.txt(8),
todo.txt-helper(8)
