# coding: utf-8
#
# This code is part of mplstyles.
#
# Copyright (c) 2022, Dylan Jones

import numpy as np
import matplotlib.pyplot as plt
from mplstyles import get_mplstyles, mplstyle_context


def plot(x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y, label="f(x)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    return fig, ax


def main():
    x = np.linspace(-10, +10, 1000)
    y = np.sin(x) / x

    for style in get_mplstyles():
        with mplstyle_context(style):
            fig, ax = plot(x, y)
            fig.savefig(f"{style}.png")


if __name__ == "__main__":
    main()
