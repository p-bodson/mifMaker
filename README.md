# mifMaker

This is a program to create an Intel Memory Initialization File (mif) containing the data necessary for representing an image via VGA on an FPGA.

The program accepts .jpg and .png files.

Each pixel in the mif will be 16 bits wide to represent 4 bits per pixel in RGBA color, regardless of whether the input image was in RGBA or not.

When using the mif for VGA output, simply ignore the alpha channel if it is not used.
