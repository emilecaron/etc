#! /bin/python3
# -*- coding: utf-8 -*-

import subprocess

from i3pystatus.core import Status

status = Status(standalone=True, reversed_register=False)

# Load (last minute)
#status.register("load",
#        critical_limit=0.5,
#        format="load:{avg1}%",)

#status.register("cpu_usage_bar")

# Ping
status.register('ping')

# CPU use
status.register("cpu_usage")

# Shows your CPU temperature, if you have a Intel CPU
status.register("temp",
    format="{temp:.0f}°C",)

# Mem use
status.register("mem",
        color="#ffffff")


# Ethernet
status.register("network",
    interface="enp3s0",
    format_up="{v4cidr}",
    color_up="#ffffff")

# Wifi
status.register("wireless",
    interface="wlp2s0",
    format_up="{essid} {quality:03.0f}% [{v4}]",
    color_up="#ffffff")

# Root disk usage
status.register("disk",
    path="/",
    format="{used}/{total}Go",)

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI 
# Salesale Pypi demande --allow-unverified et --allow-external
#status.register("pulseaudio",
#    format="♪{volume}",)


# Tue 30 Jul 11:59:46 PM KW31
status.register("clock",
    format="%a %-d %b %X KW%V",)

status.run()
