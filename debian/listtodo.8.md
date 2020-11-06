% listtodo(8)
%
% November 2020

# NAME

listtodo -- Create a context-based todo list from todo.txt task file

## SYNOPSIS

`listtodo [options]`

## DESCRIPTION

This program creates a formatted context listing of the tasks in the configured
todo.txt tasking file. The output is saved to a _.odt_ file, and is
automatically opened.

The todo.txt utility _todo.txt-helper_ is used to determine the location of the
todo.txt tasking file.

## OPTIONS
  * _-h_, _--help_ - Print help and exit
  * _-f \<FILE>\>_ - Use _\<FILE\>_ as the tasking file
  * _-p \<PRIORITY\>_ - Only show tasks with priority _\<PRIORITY\>_ or higher

## SEE ALSO
todo.txt-base(8), todo(8), edittodo(8), vitodo(8), todo.txt(8), todo.txt-helper(8)
