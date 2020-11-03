from matplotlib import image
from matplotlib import pyplot as plt
import numpy as np

def summarize(photo):
   print(f'data type = {photo.dtype}')
   print(f'data shape = {photo.shape}')
   print(f'height (vertical/row) of image = {photo.shape[0]}')
   print(f'width (horizontal/column) of image = {photo.shape[1]}')
   print(f'number of {photo.dtype} per pixel of image = {photo.shape[2]}')

def float_to_u4(photo):
   return  (photo*15).astype(np.uint8)

def u8_to_u4(photo):
   return (photo/17).round().astype(np.uint8)

def u4_to_u8(photo):
   return (photo*17).round().astype(np.uint8)

# TODO add exception catching for bad types 
def create_u4(photo):
   if photo.dtype == "float32":
      return float_to_u4(photo)
   elif photo.dtype == "uint8":
      return u8_to_u4(photo)
   else:
      return None 

#img = input('Enter name of image in current directory: ')

# load image as pixel array
data = image.imread('../morph2.png')

# summarize shape of current pixel array
print('\n' + f'CURRENT PHOTO:' + '\n')
summarize(data)

# convert pixel array to (M,N,4) shape for 16bit RGBA)

u4_data = create_u4(data)
u8_data = u4_to_u8(u4_data)

print('\n' + f'NEW PHOTO:' + '\n')
summarize(u4_data)

# save converted image for preview through FPGA 

# TODO: ask for preview image file name
#plt.imsave('images/knight_4_edit.png', u8_data)

'''
Here on converts the (M,N,4) np.array into a mif 
'''


def form_pixel(photo, row, col):
   return (f'{photo[row][col][0]:x}{photo[row][col][1]:x}{photo[row][col][2]:x}{photo[row][col][3]:x}')

def form_address(photo, row, col):
   address = row * photo.shape[1] + col
   return (f'{address:x}')

def form_u4_data(photo):
   row = photo.shape[0]
   col = photo.shape[1]
   width = photo.shape[2]

   data = []

   for current_row in range(row):
      for current_col in range(col):
         data.append( (f'{form_address(photo, current_row, current_col)}: {form_pixel(photo,current_row, current_col)}') )
   return data

def form_mif_header(depth=64,width=16,addr_radix='HEX',data_radix='HEX'):
   
   header = [
   f'DEPTH = {depth}',
   f'WIDTH = {width}',
   f'',
   f'ADDRESS_RADIX = {addr_radix}',
   f'DATA_RADIX = {data_radix}',
   f''
   ]
   return header

def form_mif_content(photo):
   content = [f'CONTENT', f'BEGIN'] + form_u4_data(photo) + [f'END']
   return content

def form_mif(photo):
   '''
   This takes the numpy.ndarray and creates the mif
   '''

   mif_str_arr = form_mif_header(photo.size, photo.shape[2]*4) + form_mif_content(photo)
   mif = '\n'.join(mif_str_arr)

   return mif

def write_mif(photo, mode='x', file='mifData.mif'):
   '''
   this writes out the mif
   '''
   f = open(file, mode)
   f.write(form_mif(photo))
   f.close()

write_mif(u4_data, 'w')

# display the array of pixels as an image

plt.imshow(data)
plt.show()
plt.imshow(u8_data)
plt.show()

