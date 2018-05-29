"""
Display random XKCD comics
"""

import os
from glob import glob
import random
import flask
import tkinter
import subprocess
from pkg_resources import resource_filename

# get screen size
root = tkinter.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find paths to all comic images, download with xkcd-dl if needed
pattern = os.path.join('xkcd_archive', '[0-9]*/*.png')
img_files = glob(pattern, recursive=True) 
if not img_files:
    subprocess.check_call(['xkcd-dl', '--update-db'])
    subprocess.check_call(['xkcd-dl', '--download-all', '--path',
                           resource_filename('xkcd_frame', '.')])
    img_files = glob(pattern, recursive=True) 

# create UI app
app = flask.Flask(__name__, static_folder='xkcd_archive')

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

    return flask.render_template(
        'index.html',
        title='{} ({})'.format(ttl, pub),
        image_file=random.choice(img_files),
        screen_width=0.95*screen_width,
        image_alt=alt
        )

# command line entry point
run = app.run
