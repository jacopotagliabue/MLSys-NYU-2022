# Week 1

## Computer Setup

1. [Installing Python](#installing-python)
2. [Virtual Environments](#virtual-environments)
3. [Demo](#demo)

## 1. Installing Python

For this course, we require you to install a version of Python that is >= version 3.7 (the latest version as of 8/27/2022 is 3.10). In practice, one may want to install multiple versions of Python such that they can use different versions for different projects. That is outside of the scope of this course, although we recommend using [pyenv](https://github.com/pyenv/pyenv) if you are interested in pursuing this.

### Mac Installation Instructions

Please follow [this section](https://realpython.com/installing-python/#how-to-install-python-on-macos) of the Real Python installation guide. We recommend going with the second installation option, using the Homebrew package manager.

#### M1/M2 Macs

If you are on a new Mac that has an M1 or M2 chip, then you will need to perform the following extra steps prior to installing Python.

1. Make sure you have installed the Homebrew package manager, and then run
    ```commandline
    brew install libomp openblas hdf5 openssl@1.1 pkg-config llvm@11
    ```
2. Add the following lines to your `~/.bashrc` or `~/.zshrc` file.
    ```
    export OPENBLAS=$(brew --prefix openblas)
    export CFLAGS="-falign-functions=8 ${CFLAGS}"
    export HDF5_DIR=$(brew --prefix hdf5)
    export LLVM_CONFIG=$(brew --prefix llvm@11)/bin/llvm-config
    ```

Lastly, please note that you should install version 3.8 or greater.

### Linux Installation Instructions

Please follow [this section](https://realpython.com/installing-python/#how-to-install-python-on-linux) of the Real Python installation guide. We recommend going with the first installation option, using your operating system's package manager.

### Windows Installation Instructions

Python is notorious for presenting difficulties to Windows users. We highly recommend using the [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/install) to run Linux on your Windows computer. If you use the WSL, then you can follow the [Linux Installation Instructions](#linux-installation-instructions) to install Python.

If you do not want to use the WSL, then beware that your professors will not be very helpful at debugging Python installation issues. Nevertheless, you can follow [this section](https://realpython.com/installing-python/#how-to-install-python-on-windows) of the Real Python installation guide.

### Testing the Installation

If you are on a Mac or Linux-based system, then you should be able to run the following command in your terminal

```commandline
python --version
```

and you should see something like `Python 3.8.12` print out (although your version may be slightly different). Make sure you _do not_ see a version less than 3 (e.g. 2.7).

You should also be able to run each of the following commands, and the _directory path_ that gets printed out should match between the two. That is, the printouts will match up until the last word, such as `/usr/bin/python` and `/usr/bin/pip`.

```commandline
which python
which pip
```

## 2. Virtual Environments

While you can do many things with Python after installing it, it's common to install "third party libraries" that provide extra functionality beyond what the "standard library" provides. Managing these third party libraries can be complicated because we may want to install different libraries for different projects. Or, we may want to install different versions of a library for different projects. To keep our projects isolated and organized, we use _virtual environments_ to manage third party libraries.

_NOTE: We highly recommend you **always** use a virtual environment when using Python. If you do not, then you are liable to mess up your "main" Python and you may have to reinstall it._

### Creating the Virtual Environment

When we create a virtual environment, we create a folder that will house all of our Python third party library files, as well as other files such as the `python` command itself. Often, you may create that folder within the folder where your project lives.

To create your first virtual environment, run the following command within this directory

```commandline
python -m venv env
```

This will create a folder called `env`. Next, run 

```commandline
source env/bin/activate
```

You have now _activated_ your virtual environment. If you run 

```commandline
which python
```

you should see that your `python` now corresponds to something like 

```
.../env/bin/python
```

Now, you can install libraries and they will be installed to this folder. When you run `python`, you will run the special virtual environment `python` from this folder. If you want to switch to a different virtual environment or leave the current one, then run 

```commandline
deactivate
```

### Installing 3rd Party Libraries

To install a third party library, we use `pip`. With your virtual environment from above activated, try running 

```commandline
pip install cowsay
```

Then, run the following code. If the [cowsay](https://pypi.org/project/cowsay/) library was installed correctly, then you should see a cow congratulating you.

```commandline
python -c 'import cowsay;cowsay.cow("Good Job!")'
```

## 3. Demo

Ok, let's try putting everything together. Navigate to the `demo` folder in your terminal (_hint: `cd demo`_). Create a new virtual environment and activate it. Then, install the _requirements_ for the demo by running

```commandline
pip install -r requirements.txt
```

This is a fast way to install multiple 3rd party libraries. The file `requirements.txt` contains a list of libraries and their associated versions or version _constraints_. By running the above command, `pip` will go through and install each library in `requirements.txt`.

Lastly, run `python plot_data.py`. You should see a plot window pop up. If you close the window, then the program will finish running. Be sure to open the `plot_data.py` file to see the code that generated the plot. While much of the code may be unfamiliar to you, see if you can get a rough idea of what's going on.

