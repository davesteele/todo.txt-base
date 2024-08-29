% listtodo(1)
%
% August 2024

# NAME

listtodo -- Create a context-based todo list from todo.txt task file

## SYNOPSIS

`listtodo [options]`

## DESCRIPTION

This program creates a formatted context listing of the tasks in the configured
todo.txt tasking file. The output is saved to a _.odt_ file, and is
automatically opened.

The default location of the todo.txt tasking file is determined by running
"todo.txt \-\-info".

## OPTIONS
  * _-h_, _\-\-help_ - Print help and exit
  * _-f \<FILE>\>_ - Use _\<FILE\>_ as the tasking file
  * _-p \<PRIORITY\>_ - Only show tasks with priority _\<PRIORITY\>_ or higher
  * _-t_ - Output the tasks to STDOUT

## SEE ALSO
todo.txt-base(8), edittodo(1), vitodo(1), listtodo(1), todo.txt(1), cdtodo(1)
