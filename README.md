# mifMaker

## Description

This is a program to create an Intel Memory Initialization File (mif) containing the data necessary for representing an image via VGA on an FPGA for use in the ECE272 class at Oregon State University.

The program accepts .jpg and .png files.

Each pixel in the mif will be 16 bits wide to represent 4 bits per pixel in RGBA color, regardless of whether the input image was in RGBA or not.

When using the mif for VGA output, simply ignore the alpha channel (the last 4 bits of the 16-bit pixel) if it is not used.

## Installation

If you've already cloned this repository into a directory, then you're pretty much done.  The next thing to do is make sure that you are using python 3 (what is used for this program) and the appropiate python modules are installed, mainly matplotlib, pillow, and numpy.  Installing matplotlib should take care of installing pillow and numpy as well

If you want, you may use put this program in a python virtual environment and install the dependencies there.

## How to use

After this program is cloned into a directoy, simply place the image you want to convert into the same directory as mifMaker.py.

Then run the script as

    python3 mifMaker.py

*replace python3 with whatever command is used to instantiate a python3 REPL.  Many systems use "python" for python 2, and "python3" for python 3.*

The script will ask you for the name of image. **Be sure to include the file extension.**

When asked for a location to save the preview image, **be sure to include the file extension.**

- Remember that the resolution through VGA is limited, make sure that the image being converted to mif is small enough to fit on a VGA screen