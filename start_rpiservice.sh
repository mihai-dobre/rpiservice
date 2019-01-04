#!/bin/bash

# Check if gedit is running
# -x flag only match processes whose name (or command line if -f is
# specified) exactly match the pattern.

if pgrep -x "python3.6" > /dev/null
then
    echo "Running"
else
    /usr/local/bin/python3.6 /home/pi/rpiservice/main.py
fi