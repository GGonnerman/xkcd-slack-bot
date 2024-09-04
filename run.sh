#!/bin/bash

# Short little script that you can run from a cron job
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"
"$SCRIPT_DIR/env/bin/python" "$SCRIPT_DIR/main.py"
