# mifMaker

## Description

This is a program to create an Intel Memory Initialization File (mif) containing the data necessary for representing an image via VGA on an FPGA for use in the ECE272 class at Oregon State University.

The program accepts .jpg , .png , and .bmp files.

Each pixel in the mif will be 16 bits wide to represent 4 bits per pixel in RGBA color, regardless of whether the input image was in RGBA or not.

When using the mif for VGA output, simply ignore the alpha channel (the last 4 bits of the 16-bit pixel) if it is not used.

**Attention:** The output of the program is limited to 256x256 pixels to ensure a maximum of 65536 words, which is the maximum size of a ROM block using the Quartus II Prime ROM creation tool.  Any dimensions of an image larger that 256 pixels will be cropped to 256.

## Installation

> *If you would like to see a video explaining how to use this program, see the Tutorials posted on the ECE 272 Lab page https://eecs.oregonstate.edu/tekbots/courses/ece272*

If you've already cloned this repository into a directory, nice job. Otherwise, to clone this repository, simply change into the directory where you want the repository to exist, make sure git is installed, and type

    git clone https://github.com/p-bodson/mifMaker.git 

A folder named mifMaker should appear which contains the relevant scripts.

The next thing to do is make sure that you are using python 3 (it is used for this program) and the appropiate python modules are installed, mainly matplotlib, pillow, and numpy.  Installing matplotlib should take care of installing pillow and numpy as well

If you want, you may put this program in a python virtual environment and install the dependencies there.

## How to use

After this program is cloned follow these step inside the same directory as *mifMaker.py*:

1. Place the image you want to convert into the same directory as mifMaker.py.
2. Run the chmod command to ensure that mifMaker.py is executable (if it is not already executable)

         chmod 744 mifMaker.py

3. Run the script with

         python3 mifMaker.py

*Replace python3 with whatever command is used to instantiate a python3 REPL.  Many systems use "python" for python 2, and "python3" for python 3.*

### Things to consider

- The script will ask you for the name of image. **Be sure to include the file extension.**

> This means writing *my_image.png* instead of *my_image*

- When asked for a location to save the preview image, **be sure to include the file extension.**

> This means writing *my_preview_image.png* instead of *my_preview_image*

- The mif will be saved as mifData.mif in the same directory as mifMaker.py. If you run the program again, **the data will be overwritten** 
