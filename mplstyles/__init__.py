# coding: utf-8
#
# This code is part of mplstyles.
#
# Copyright (c) 2022, Dylan Jones

import os
import pkg_resources
import matplotlib.pyplot as plt
from .cycler import set_colorcycle, set_prop_cycle

try:
    from ._version import __version__
except ImportError:
    __version__ = "0.0.0"

_initialized = False


def get_mplstyles():
    ext = ".mplstyle"
    styles_dir = pkg_resources.resource_filename("mplstyles", "styles")
    styles = list()
    for root, _, files in os.walk(styles_dir):
        for filename in files:
            if filename.endswith(ext):
                name = filename.removesuffix(ext)
                styles.append(name)
    return styles


def register_style_dir(path):
    """Register the styles in a directory with matplotlib."""
    stylesheets = plt.style.core.read_style_directory(path)
    plt.style.core.update_nested_dict(plt.style.library, stylesheets)


def register_styles(styles_root_dir):
    """Register the styles in a nested directory with matplotlib."""
    global _initialized

    # Reads in defined styles
    stylesheets = plt.style.core.read_style_directory(styles_root_dir)
    for root, dirs, _ in os.walk(styles_root_dir):
        for dirname in dirs:
            path = os.path.join(root, dirname)
            new_stylesheets = plt.style.core.read_style_directory(path)
            stylesheets.update(new_stylesheets)

    # Update dictionary of styles
    plt.style.core.update_nested_dict(plt.style.library, stylesheets)
    _initialized = True


def init_mplstyles():
    register_styles(pkg_resources.resource_filename("mplstyles", "styles"))


def use_mplstyle(*name, color_cycle=None, ls_cycle=None, lw_cylce=None):
    if not _initialized:
        init_mplstyles()
    plt.style.use(name)
    set_prop_cycle(color_cycle, ls_cycle, lw_cylce)


def mplstyle_context(*name):
    if not _initialized:
        init_mplstyles()
    return plt.style.context(name)
