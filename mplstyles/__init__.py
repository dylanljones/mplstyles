# coding: utf-8
#
# This code is part of mplstyles.
#
# Copyright (c) 2022, Dylan Jones

import os
import matplotlib.pyplot as plt

try:
    from ._version import __version__
except ImportError:
    __version__ = "0.0.0"


def use_mplstyle(name: str) -> None:
    name = os.path.splitext(name)[0] + ".mplstyle"  # ensure the name ends with ext
    file = os.path.join(os.path.dirname(__file__), name)
    plt.style.use(file)


def mplstyle_context(name: str):
    name = os.path.splitext(name)[0] + ".mplstyle"  # ensure the name ends with ext
    file = os.path.join(os.path.dirname(__file__), name)
    return plt.style.context(file)


def get_mplstyles():
    names = list()
    for name in os.listdir(os.path.dirname(__file__)):
        if os.path.splitext(name)[1] == ".mplstyle":
            names.append(name)
    return names
