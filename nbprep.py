import os

import matplotlib.pyplot as plt
from IPython.core.display import display, HTML, Javascript

def style(dpi=120):
    plt.rc('savefig', dpi=dpi)

    css_file = './static/custom.css'
    css_txt = open(css_file, "r").read()
    css = HTML(css_txt)
    display( css )
# Uncomment this stuff for equation numbering
#    mathjax = \
#'''
#MathJax.Hub.Config({
#  TeX: { equationNumbers: { autoNumber: "AMS" } }
#});
#'''
#    display( Javascript(mathjax))
    
def dump_sync(folder='.'):
    files = os.listdir(folder)
    [os.remove(os.path.join(folder, i)) for i in files if 'syncdoc' in i]
