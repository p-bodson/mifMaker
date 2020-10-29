from matplotlib import image
from matplotlib import pyplot as plt
import numpy as np

def summarize(photo):
   print(f'data type = {data.dtype}')
   print(f'data shape = {data.shape}')
   print(f'height (vertical/row) of image = {data.shape[0]}')
   print(f'width (horizontal/column) of image = {data.shape[1]}')
   print(f'number of {data.dtype} per pixel of image = {data.shape[2]}')

def float_to_u4(photo):
   return  (photo*15).round().astype(np.uint8)

def u8_to_u4(photo):
   return (photo/255*15).round().astype(np.uint8)

def print_row_4_float(photo, row):
   coord = [None,None,None,None] 
   for value in range(photo.shape[1]):
      for num in range(photo.shape[2]): 
         coord[num] = photo[row][value][num]
      print(f'{row:x}-{value:x}: {coord[0]:x}{coord[1]:x}{coord[2]:x}{coord[3]:x}')

def print_row_3_u4(photo, row):
   coord = [None,None,None] 
   for value in range(photo.shape[1]):
      for num in range(photo.shape[2]): 
         coord[num] = photo[row][value][num]
      print(f'{row:x}-{value:x}: {coord[0]:x}{coord[1]:x}{coord[2]:x}')


#img = input('Enter name of image in current directory: ')
# load image as pixel array
data = image.imread('images/knight_4.png')
# summarize shape of the pixel array


summarize(data)

float_data = float_to_u4(data)
u4_data = u8_to_u4(data)


#print_row_4_float(float_data, 100)
#print_row_3_u4(u4_data, 100)


# display the array of pixels as an image
plt.imshow(data)
plt.show()
plt.imshow(float_data)
plt.show()
