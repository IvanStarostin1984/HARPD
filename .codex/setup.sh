#!/bin/bash
set -e
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

echo "Setup complete"
