#!/bin/bash
xkcd-frame &
sleep 60
midori -e Fullscreen -e Navigationbar -a http://localhost:5000 &
