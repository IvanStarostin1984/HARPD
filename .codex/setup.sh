#!/usr/bin/env bash
# Install Python packages if requirements.txt exists
if [ -f requirements.txt ]; then
  pip install -r requirements.txt
fi
