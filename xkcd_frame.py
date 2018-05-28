"""
Display random XKCD comics
"""

import os
from glob import glob
import random
import flask
import tkinter

# constants - replace with cmdline parameters
ROOT_PATH = '~/prj/xkcd-frame/xkcd_archive'
INTERVAL = 60 # seconds

# get screen size
root = tkinter.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find paths to all comic images, as downloaded by xkcd-dl
img_files = glob(os.path.join('static', '[0-9]*/*.png'), recursive=True) 

# create UI app
app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def ui():
    # select image file and read alt text
    img = random.choice(img_files)
    with open(os.path.dirname(img) + '/description.txt', 'r') as fp:
        lines = fp.readlines()
    alt = ""
    for line in lines:
        if line[:4] == 'alt:':
            alt = line[4:].strip()
            break

    return flask.render_template(
        'index.html',
        image_file=random.choice(img_files),
        image_width=0.95*screen_width,
        image_alt=alt
        )

app.run()
