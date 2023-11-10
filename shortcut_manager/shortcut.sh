#!/bin/bash
SCRIPT_MANAGER="$SCRIPT_MANAGER_PATH"
SCRIPT_SHORTCUTS="/usr/local/bin/shortcuts.json"

if [ "$#" -gt 3 ]; then
    echo 'Too many arguments'
elif [ "$1" = "add" ]; then
    python3 "$SCRIPT_MANAGER" add "$2" "$3"
elif [ "$1" = "open" ]; then
    python3 "$SCRIPT_MANAGER" open "$2"

elif [ "$#" -lt 2 ]; then
    echo 'Usage: ./run.sh add {shortcut} {url}  OR  ./run.sh open {shortcut}'
fi
