#!/bin/bash

""":"
PREFERRED_PYTHONS="python3.11 python3.10 python3.9 python3.8 python3.7 python3.6 python3.5 python3"
for cmd in "${PYTHON:-}" ${PREFERRED_PYTHONS}; do
    if command -v > /dev/null "$cmd"; then
        PYTHON="$(command -v "$cmd")"
        echo L is $PYTHON
        echo cmd is $cmd
        exec "${PYTHON}" "$0" "$@"
    fi


done
echo error: lmake could not find a python interpreter!" >&2
exit 1
":"""


import sys

if __name__ == '__main__':
    print('this is test')
    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2])

