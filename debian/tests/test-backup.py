#!/bin/sh

set -e

if [ -z "$AUTOPKGTEST_ARTIFACTS" ] ; then
  BASEDIR=/tmp
else
  BASEDIR=$AUTOPKGTEST_ARTIFACTS
fi

TESTDIR="$BASEDIR"/backuptest
rm -rf "$TESTDIR"
mkdir "$TESTDIR"

TODO="$TESTDIR"/todo.txt
echo "Foo" > "$TODO"

BACKUPDIR="$TESTDIR/backup"
mkdir "$BACKUPDIR"

backuptodo -f "$TODO" -b "$BACKUPDIR"

cat "$BACKUPDIR"/* | grep -q "Foo"

echo "Test complete"
