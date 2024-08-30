% vitodo(1)
%
% August 2024

# NAME

vitodo -- Edit the configured todo.txt tasking file using vi

## SYNOPSIS

`vitodo`

## DESCRIPTION

This command opens the configured todo.txt tasking file using "vi".

Hooks are provided that can be run before and after todo.txt file processing.
Scripts run before processing are to be stored in
_/etc/todo.txt-base/prehooks_. Scripts run after processing are stored in
_/etc/todo.txt-base/posthooks_. All scripts are run with a single argument
defining the location of the todo.txt tasking file.

The location of the todo.txt tasking file is determined by running "todo.txt
\-\-info".

## SEE ALSO

todo.txt-base(8), edittodo(1), listtodo(1), todo.txt(1), cdtodo(1), backuptodo(1)
