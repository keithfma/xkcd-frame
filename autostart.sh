#!/bin/bash
cd /home/pi/xkcd-frame
./xkcd_frame.py &
sleep 60
midori -e Fullscreen -e Navigationbar -a http://localhost:5000 &
