# coding: utf-8
#
# This code is part of mplstyles.
#
# Copyright (c) 2022, Dylan Jones

import os.path
import numpy as np
import matplotlib.pyplot as plt
from mplstyles import get_mplstyles, init_mplstyles

init_mplstyles()


def plot(x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y, label="f(x)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    return fig, ax


def main():
    x = np.linspace(-4 * np.pi, +4 * np.pi, 1000)
    y = np.sin(x) / x

    style_list = [
        ["plot"],
        ["figure"],
        ["plot", "aps"],
        ["plot", "aps", "aps1.5"],
        ["plot", "aps", "aps2"],
        ["figure", "aps"],
        ["figure", "aps", "aps1.5"],
        ["figure", "aps", "aps2"],
    ]

    figdir = "figures"
    if not os.path.exists(figdir):
        os.makedirs(figdir)

    for styles in style_list:
        file = "_".join(styles) + ".png"
        with plt.style.context(styles):
            fig, ax = plot(x, y)
            print(f"Saving {file}")
            fig.savefig(os.path.join(figdir, file))


if __name__ == "__main__":
    main()
