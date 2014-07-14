#!/bin/bash

export DE=i3

# Enable numlock
numlockx &

# Dbus fix
if [ -z "$DBUS_SESSION_BUS_ADDRESS" ]; then
    eval "$(dbus-launch --sh-syntax --exit-with-session)"
fi

exec i3
#exec i3 -V >> ~/.i3/i3log 2>&1
