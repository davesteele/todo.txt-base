% vitodo(1)
%
% August 2024

# NAME

backuptodo -- Make a backup archive of the todo.txt task file

## SYNOPSIS

`backuptodo [options]`

## DESCRIPTION

This command will make snapshot backups of the todo.txt file to a backup folder.

A specified number of backups will be kept. Older snapshots will be removed.

Hooks are provided that can be run before and after todo.txt file processing.
Scripts run before processing are to be stored in
_/etc/todo.txt-base/prehooks_. Scripts run after processing are stored in
_/etc/todo.txt-base/posthooks_. All scripts are run with a single argument
defining the location of the todo.txt tasking file.

## OPTIONS
  * _-h_, _\-\-help_ - Print help and exit
  * _-f \<FILE\>_ - Use _\<FILE\>_ as the tasking file
  * _-b \<BACKUPDIR\>_ - Place shapshots in this directory (defaults to Dropbox "todo/backup").
  * _-n \<NUM\>_ - keep _<NUM>_ snapshots
  * _-c \<CONFIG\>_ - alternate config file location

## SEE ALSO

todo.txt-base(8), edittodo(1), listtodo(1), todo.txt(1), cdtodo(1), vitodo(1)

