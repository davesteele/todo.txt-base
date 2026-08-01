% justone(1)
%
% Aug 2027

# NAME

justone -- Display a single random active todo.txt task

## SYNOPSIS

justone \[ \<ARG\> ... \]

## DESCRIPTION

This command returns a single active task in the configured todo.txt tasking
file.

Tasks are identified as lines in the tasking file which contain a "@" symbol.
Comment lines (lines containing a "#") are excluded.

Arguments are passed on to the todo.txt command. They can be used to limit
the pool of candidate tasks.

The location of the todo.txt tasking file is determined by running "todo.txt
\-\-info".

## SEE ALSO

todo.txt(1), tdt(1), todo.txt-base(8), edittodo(1), listtodo(1), cdtodo(1),
backuptodo(1), vitodo(1)
