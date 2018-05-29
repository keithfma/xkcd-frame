#!/usr/bin/env python3
"""
Display random XKCD comics
"""

import os
from glob import glob
import random
import flask
import tkinter
import subprocess

# get screen size
root = tkinter.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find paths to all comic images, download with xkcd-dl if needed
pattern = os.path.join('static', 'xkcd_archive', '[0-9]*/*.png')
img_files = glob(pattern, recursive=True)

# create app
app = flask.Flask('xkcd-frame')

@app.route('/', methods=['GET'])
def ui():
    # select image file
    img = random.choice(img_files)
    # read metadata
    with open(os.path.dirname(img) + '/description.txt', 'r') as fp:
        lines = fp.readlines()
    alt = ""
    for line in lines:
        if line[:7] == 'title :':
            ttl = line[7:].strip()
        elif line[:15] == 'date-published:':
            pub = line[15:].strip()
        elif line[:4] == 'alt:':
            alt = line[4:].strip()
    # build page
    return flask.render_template(
        'main.html',
        title='{} ({})'.format(ttl, pub),
        image_file='/' + img,
        screen_width=0.95*screen_width,
        image_alt=alt
        )

if __name__ == '__main__':
    app.run()

