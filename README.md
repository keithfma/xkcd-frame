# XKCD Digital Picture Frame

This repo contains software and instructions to set up a simple digital picture
frame that displays a random XKCD comic, refreshed on some preset interval.

## Hardware

I used the following hardware, though many many other configurations would likely work:

+ Raspberry Pi Zero W circa May 2018: DETAIL, LINK
+ LANDZO 3.5" LCD screen: DETAILS, LINK
+ MicroSD card: DETAILS, LINK
+ Case, power supply, etc from a kit: LINK

## System Setup

I set up a "headless" system (i.e., without a monitor, keyboard, etc.). The OS
is Raspian VERSION. There are more complete guides to this process out and
about on the web, but here are the key steps I used: 

+ Solder the pin connectors to the pi board: LINK
+ Download the Raspbian image: LINK
+ Download Etcher: Link
+ Flash the OS onto the SD card
+ Insert the SD card, and connect the screen to the board (just push in the pins)
+ Supply the wireless login information by adding a `wpa_supplicant.conf` file
  to the boot partition. The contents should be something like: ADD DETAILS
+ Enable SSH access by adding an empty file named `ssh` to the boot partition.
+ Power up!
+ Find the IP address of the pi. First, I found my own IP address with
  `ifconfig`, then I ran a scan on a range of local IPs using Angry IP scanner
  (LINK). 
+ SSH into the pi using the default username and password (pi, raspberry, respectively)
+ Update everything (sudo apt update; sudo apt upgrade)
+ Add user `pi` to group `tty`, otherwise the desktop will not load: `usermod -a -G tty pi`
+ Install drivers for the LCD screen. These are provided by a kind soul on
  github: LINK. To use them I cloned the repo, added execute permissions to
  LCD35-show, and executed it.
+ Reboot!

Voila, a working Pi Zero system. Though I expect anyone reading this will find
new and exciting problems to solve along the way.

## xkcd-frame Software

TBD

You need to download the XKCD images with `xkcd-dl`. Navigate to the `static`
folder, and run `xkcd-dl -a`.

## Enable xkcd-frame on Boot

https://blog.gordonturner.com/2017/07/22/raspberry-pi-full-screen-browser-raspbian-july-2017/

midori -e Fullscreen -e Navigationbar -a http://localhost:5000
