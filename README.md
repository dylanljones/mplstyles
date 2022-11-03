# Matplotlib styles for scientific computing


## Installation

Install from GitHub via
```commandline
pip install git+https://github.com/dylanljones/mplstyles.git@VERSION
```
where `VERSION` is a release, tag or branch name.

## Introduction

Matplotlib allows you to customize the properties and default styles of plots.  
There are three ways to customize Matplotlib (see [mplstyle] for more information):
- [Setting rcParams at runtime](https://matplotlib.org/stable/tutorials/introductory/customizing.html#customizing-with-dynamic-rc-settings)
- [Using style sheets](https://matplotlib.org/stable/tutorials/introductory/customizing.html#customizing-with-style-sheets)
- [Changing your matplotlibrc file](https://matplotlib.org/stable/tutorials/introductory/customizing.html#customizing-with-matplotlibrc-files)

> **Warning**: Setting rcParams at runtime takes precedence over style sheets, 
style sheets take precedence over ``matplotlibrc`` files.

This project uses the third option and is intended as a collection of usefull 
matplotlibrc style files for scientific plotting.

> **Note**: If you are using PyCharm to edit the ``*.mplstyle`` files, right-click on the file 
and click 'Override File Type'. There, choose the ``Ini`` file-type. This enables
some synthax highlighting, whcich makes it easier to find enables sections.

## Usage

The rc-files are contained in the ``mplstyles`` package. In general, any matplotlibrc file
can be loaded via
````python
import matplotlib.pyplot as plt

plt.style.use("file.mplstyle")
````

The included styles of ``mplstyles`` can be applied with the ``use_mplstyle`` method:
````python
from mplstyles import use_mplstyle

use_mplstyle("figures")
````

A list of all included style files can be printed like this:
````python
from mplstyles import get_mplstyles

print(get_mplstyles())
````

## Examples

### ``figures.mplstyle``


### ``plots.mplstyle``


[mplstyle]: https://matplotlib.org/stable/tutorials/introductory/customizing.html
