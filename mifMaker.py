import os
try:
    from matplotlib import image
    import numpy as np
except:
    os.system('pip3 install -r requirements.txt')
    from matplotlib import image
    import numpy as np

from helpers import summarize, create_u4, create_preview, write_mif

# load image as pixel array
img = input('Enter name of image relative to current directory: ')
data = image.imread(img)

# create data for VGA from image array
uint4_data = create_u4(data)

summarize(data, 'ORIGINAL DATA:')
summarize(uint4_data, 'MIF DATA')

# save converted image for preview before placing on FPGA
create_preview(uint4_data)

# save the data for the mif
write_mif(uint4_data, 'w')
