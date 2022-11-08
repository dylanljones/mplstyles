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


def get_mplstyles():
    names = list()
    for name in os.listdir(os.path.dirname(__file__)):
        if os.path.splitext(name)[1] == ".mplstyle":
            names.append(name)
    return names


def _get_style(name: str):
    filename = name
    ext = ".mplstyle"
    if not filename.endswith(ext):
        # ensure the name ends with ext
        filename = filename + ext
    file = os.path.join(os.path.dirname(__file__), filename)
    if not os.path.exists(file):
        styles = ", ".join(f"'{x}'" for x in get_mplstyles())
        raise ValueError(
            f"Input '{name}' is not a valid style! Supported styles are {styles}"
        )
    return file


def use_mplstyle(name: str):
    file = _get_style(name)
    plt.style.use(file)


def mplstyle_context(name: str):
    file = _get_style(name)
    return plt.style.context(file)
