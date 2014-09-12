import os

import matplotlib.pyplot as plt
from IPython.core.display import display, HTML

def style(dpi=120):
    plt.rc('savefig', dpi=dpi)
    css_file = './static/custom.css'
    css = HTML(open(css_file, "r").read())
    display( css )
    
def dump_sync(folder='.'):
    files = os.listdir(folder)
    [os.remove(os.path.join(folder, i)) for i in files if 'syncdoc' in i]
