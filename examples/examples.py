# coding: utf-8
#
# This code is part of mplstyles.
#
# Copyright (c) 2022, Dylan Jones

import numpy as np
import matplotlib.pyplot as plt
from mplstyles import get_mplstyles, mplstyle_context


def main():
    x = np.linspace(-5, +5, 1001)
    y = np.sin(x)

    for style in get_mplstyles():
        with mplstyle_context(style):
            fig, ax = plt.subplots()
            ax.plot(x, y)
            fig.savefig(f"{style}.png")


if __name__ == "__main__":
    main()
