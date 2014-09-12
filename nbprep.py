import matplotlib.pyplot as plt
from IPython.core.display import display, HTML

def style(dpi=120):
    plt.rc('savefig', dpi=dpi)
    css_file = './static/custom.css'
    css = HTML(open(css_file, "r").read())
    display( css )
    

