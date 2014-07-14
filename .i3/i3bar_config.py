#! /bin/python3
# -*- coding: utf-8 -*-

from i3pystatus.core import Status

status = Status(standalone=True, reversed_register=False)

# i3 shift
status.register('i3shift')

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
    format_up="{essid} {quality:3.0f}% [{v4}]",
    color_up="#ffffff")

# Root disk usage
status.register("disk",
    path="/",
    format="{used}/{total}Go",)


# Date and time 
status.register("clock",
    format="%a %-d %b %X Week%V",)

status.run()
