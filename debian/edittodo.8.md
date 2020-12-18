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

The location of the todo.txt tasking file is determined by running "todo.txt
\-\-info".

## SEE ALSO

todo.txt-base(8), vitodo(8), listtodo(8), todo(8), todo.txt(8)
