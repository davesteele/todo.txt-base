% todo.txt-base(8)
%
% November 2020

# NAME

todo.txt-base -- Extension support for todo.txt packages

## SYNOPSIS

`todo.txt-base {pre|post} <taskfile>`

## DESCRIPTION

This command adds extension hook support to _todo.txt_ applications.

With the _pre_ argument, scripts found in the _/etc/todo.txt-base/prehooks/_
directory are run. With the _post_ argument, scripts found in the
_/etc/todo.txt-base/posthooks/_ directory are run. Scripts are run in
alphabetical order. Each script is given a single argument with the full path
to the todo.txt tasking file.

## SEE ALSO

vitodo(1), edittodo(1), listtodo(1), todo.txt(1)
