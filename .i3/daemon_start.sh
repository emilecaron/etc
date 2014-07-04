#!/bin/sh

mkfifo /tmp/daemon_input
python ~/.i3/lemonde_daemon.py </tmp/daemon_input 
#cat /tmp/daemon_input | python lemonde_daemon.py
