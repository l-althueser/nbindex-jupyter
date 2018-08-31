import os
import sys
import time
from pathlib import Path
from IPython.display import display, HTML, Javascript

def combine(*html_objects):
    """
    Combines different HTML objects for use in a single cell
    """
    return HTML(''.join([o.data for o in html_objects]))

def save_notebook():
    """
    Save current IPython notebook.
    """
    return display(Javascript("IPython.notebook.save_notebook()"))

def checkpoint_notebook():
    """
    Checkpoint current IPython notebook.
    """
    return display(Javascript("IPython.notebook.save_checkpoint()"))

def cells_width(width=90, margin_left=5):
    """
    Set Jupyter notebook cell width to certain value (10-100)
    """
    if width < 20:
        raise(ValueError("Invalid value for <width>!"))

    display(HTML("<style>.container {{ width:{0}% !important; \
                  margin-left: {1}% !important;}}</style>".format(width,
                                                                  margin_left)))

def cells_centered():
    """
    Center output cells.
    """
    CSS = """
    .output_png img {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    """
    display(HTML('<style>{0}</style>'.format(CSS)))
