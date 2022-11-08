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

Please feel free to add your own favourite styles to the libary! Start from the empty 
template file ``default.mplstyle`` and change the parameters you like.
If you are happy with the style, add the file to the ``mplstyles`` package and open 
a pull request. 


> **Note**: If you are using PyCharm to edit the ``*.mplstyle`` files, right-click on the file
and click 'Override File Type'. There, choose the ``Ini`` file-type. This enables
some synthax highlighting, which makes it easier to find uncommented sections.

## Usage

The rc-files are contained in the ``mplstyles`` package. In general, any matplotlibrc file
can be loaded via
````python
import matplotlib.pyplot as plt

plt.style.use("/full/path/to/file.mplstyle")
````

The included styles of ``mplstyles`` can be applied with the ``use_mplstyle`` method:
````python
from mplstyles import use_mplstyle

use_mplstyle("figures.mplstyle")  # with file extension
use_mplstyle("figures")           # or without file extension
````

A list of all included style files can be printed like this:
````python
from mplstyles import get_mplstyles

print(get_mplstyles())
````

## Examples

All examples are generated with the following code and by applying the different styles:
````python
fig, ax = plt.subplots()
ax.plot(x, y, label="f(x)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
````

### ``plots.mplstyle``

Style for developing

<p align="center">
  <img src="https://raw.githubusercontent.com/dylanljones/mplstyles/master/examples/plots.mplstyle.png" alt="figures.mplstyle example" style="width: 400px" />
</p>


### ``aps.mplstyle``

Style for generatig single-column figures for APS journals (physical review, ...)

<p align="center">
  <img src="https://raw.githubusercontent.com/dylanljones/mplstyles/master/examples/aps.mplstyle.png" alt="aps.mplstyle example" style="width: 400px" />
</p>


### ``aps1.5.mplstyle``

Style for generatig 1.5-column figures for APS journals (physical review, ...)

<p align="center">
  <img src="https://raw.githubusercontent.com/dylanljones/mplstyles/master/examples/aps1.5.mplstyle.png" alt="aps1.5.mplstyle example" style="width: 400px" />
</p>


### ``aps2.mplstyle``

Style for generatig double-column figures for APS journals (physical review, ...)

<p align="center">
  <img src="https://raw.githubusercontent.com/dylanljones/mplstyles/master/examples/aps2.mplstyle.png" alt="aps2.mplstyle example" style="width: 400px" />
</p>



[mplstyle]: https://matplotlib.org/stable/tutorials/introductory/customizing.html
