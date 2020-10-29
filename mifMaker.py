from matplotlib import image
from matplotlib import pyplot as plt
import numpy as np

def summarize(photo):
   print(f'data type = {photo.dtype}')
   print(f'data shape = {photo.shape}')
   print(f'height (vertical/row) of image = {photo.shape[0]}')
   print(f'width (horizontal/column) of image = {photo.shape[1]}')
   print(f'number of {photo.dtype} per pixel of image = {photo.shape[2]}')

def print_row_4_u4(photo, row):
   coord = [None,None,None,None] 
   for value in range(photo.shape[1]):
      for num in range(photo.shape[2]): 
         coord[num] = photo[row][value][num]
      print(f'{row:x}-{value:x}: {coord[0]:x} {coord[1]:x} {coord[2]:x} {coord[3]:x}')

def print_row_3_u4(photo, row):
   coord = [None,None,None] 
   for value in range(photo.shape[1]):
      for num in range(photo.shape[2]): 
         coord[num] = photo[row][value][num]
      print(f'{row:x}-{value:x}: {coord[0]:x} {coord[1]:x} {coord[2]:x}')

def print_row_4_float(photo, row):
   coord = [None,None,None,None] 
   for value in range(photo.shape[1]):
      for num in range(photo.shape[2]): 
         coord[num] = photo[row][value][num]
      print(f'{row:}-{value:}: {coord[0]} {coord[1]} {coord[2]} {coord[3]}')

def round_off(photo):
   return (photo*255).astype(np.uint8)

def float_to_u4(photo):
   return  (photo*15).astype(np.uint8)

def u8_to_u4(photo):
   return (photo/17).round().astype(np.uint8)

def u4_to_u8(photo):
   return (photo*17).round().astype(np.uint8)


#img = input('Enter name of image in current directory: ')
# load image as pixel array
data = image.imread('images/knight_4.png')
# summarize shape of the pixel array


#summarize(data)

float_data = float_to_u4(data)
#u4_data = u8_to_u4(data)
u8_data = u4_to_u8(float_data)
#rounded_data = round_off(data)

summarize(float_data)
'''
#print_row_4_u4(float_data, 100)
#print_row_4_u4(u4_data, 100)
#print_row_4_u4(u8_data,100)
#print_row_4_float(rounded_data, 100)
print_row_4_float(data, 100)
print_row_4_float(float_data, 100)
print_row_4_float(float_data*17,100)
print_row_4_u4(u8_data,100)
'''
#print_row_4_u4(u8_data,100)

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

def form_mif_header(depth=64,width=12,addr_radix='HEX',data_radix='HEX'):
   
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



def write_mif(photo, mode='x', file='mifs/mifData.mif'):
   '''
   this writes out the mif
   '''
   f = open(file, mode)
   f.write(form_mif(photo))
   f.close()

write_mif(float_data, 'w')




# display the array of pixels as an image

#plt.imshow(data)
#plt.show()


#plt.imshow(u8_data)
#plt.show()
#plt.imsave('images/knight_4_edit.png', u8_data)

