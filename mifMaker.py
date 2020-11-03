from matplotlib import image
import numpy as np
from helpers import summarize, create_u4, create_preview, write_mif, prepare_data

# load image as pixel array
img = input('Enter name of image relative to current directory: ')
data = image.imread(img)

# make array into appropriate size for next steps
new_data = prepare_data(data)

# create data for VGA from image array
uint4_data = create_u4(new_data)

summarize(data, 'ORIGINAL DATA:')
summarize(uint4_data, 'MIF DATA')
#summarize(new_data, 'PREPARED DATA:')
#summarize(data, 'ORIGINAL DATA:')

# save converted image for preview before placing on FPGA
create_preview(uint4_data)

# save the data for the mif
write_mif(uint4_data, 'w')
