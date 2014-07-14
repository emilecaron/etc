#!/bin/bash

#export DE=openbox
export DE=i3

numlockx &

# Dbus fix
if [ -z "$DBUS_SESSION_BUS_ADDRESS" ]; then
    eval "$(dbus-launch --sh-syntax --exit-with-session)"
fi

#/usr/bin/xdg-user-dirs-update

# start openbox
#/usr/bin/openbox-session > ~/.openbox_startup.log >&1

#exec i3 -V >> ~/.i3/i3log 2>&1
exec i3
