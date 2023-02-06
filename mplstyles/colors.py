# coding: utf-8
#
# This code is part of mplstyles.
#
# Copyright (c) 2023, Dylan Jones

"""Special color cycles for matplotlib."""

from typing import Sequence, Union
import matplotlib as mpl
import matplotlib.pyplot as plt

seaborn_colorblind = ["#0072B2", "#009E73", "#D55E00", "#CC79A7", "#F0E442", "#56B4E9"]
tableau_colorblind = [
    "#006BA4",
    "#FF800E",
    "#ABABAB",
    "#595959",
    "#5F9ED1",
    "#C85200",
    "#898989",
    "#A2C8EC",
    "#FFBC79",
    "#CFCFCF"
]

cycles = {
    "seaborn-colorblind": seaborn_colorblind,
    "tableau-colorblind": tableau_colorblind,
}


def set_colorcycle(color: Union[Sequence, str]) -> None:
    if isinstance(color, str):
        color = cycles[color]
    mpl.rcParams["axes.prop_cycle"] = mpl.cycler(color=color)


def show_greyscale(file):
    import numpy as np
    from PIL import Image

    image = Image.open(file).convert("L")

    fig, ax = plt.subplots()
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.imshow(np.asarray(image), cmap='gray', vmin=0, vmax=255)  # noqa
    return fig, ax
