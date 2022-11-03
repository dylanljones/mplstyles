# coding: utf-8
#
# This code is part of mplstyles.
#
# Copyright (c) 2022, Dylan Jones

import os
import matplotlib.pyplot as plt


def use_mplstyle(name: str) -> None:
    name = os.path.splitext(name)[0] + ".mplstyle"  # ensure the name ends with ext
    plt.style.use(os.path.join(os.path.dirname(__file__), name))


def get_mplstyles():
    names = list()
    for name in os.listdir(os.path.dirname(__file__)):
        if os.path.splitext(name)[1] == ".mplstyle":
            names.append(name)
    return names
