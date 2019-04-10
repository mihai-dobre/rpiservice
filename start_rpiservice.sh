#!/bin/bash

# Check if gedit is running
# -x flag only match processes whose name (or command line if -f is
# specified) exactly match the pattern.

# crontab rule:
# */1 * * * * /bin/bash /home/pi/rpiservice/start_rpiservice.sh >> /var/log/rpiservice.log 2>&1
# do not forget to create the /var/log/rpiservice.log file

if pgrep -x "python3.4" > /dev/null
then
    echo "Running"
else
    /usr/bin/python3.4 /home/pi/rpiservice/main.py
fi
