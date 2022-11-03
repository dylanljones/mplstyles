# coding: utf-8
#
# This code is part of mplstyles.
#
# Copyright (c) 2022, Dylan Jones

import numpy as np
import matplotlib.pyplot as plt
from mplstyles import mplstyle_context

STYLES = "figures.mplstyle", "plots.mplstyle"


def main():
    x = np.linspace(-5, +5, 1001)
    y = np.sin(x)
    for style in STYLES:
        with mplstyle_context(style):
            fig, ax = plt.subplots()
            ax.plot(x, y)
            fig.savefig(f"{style}.png")


if __name__ == "__main__":
    main()
