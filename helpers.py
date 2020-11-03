from matplotlib import pyplot as plt
import numpy as np


def summarize(photo, title='DATA:'):
    print('\n' + f'{title}' + '\n')
    print(f'array: {photo}') 
    print(f'data type = {photo.dtype}')
    print(f'data shape = {photo.shape}')
    print(f'data size = {photo.size}')
    #print(f'data dimension = {photo.ndim}')
    print(f'height (vertical/row) of image = {photo.shape[0]}')
    print(f'width (horizontal/column) of image = {photo.shape[1]}')
    #print(f'number of {photo.dtype} per pixel of image = {photo.shape[2]}') # does not work for luminance photos

def float_to_u8(photo):
   return  (photo*255).astype(np.uint8)

def u4_to_u8(photo):
   return (photo*17).round().astype(np.uint8)

def solid_layer(photo, value = 255):
    initial_layer = np.zeros((photo.shape[0],photo.shape[1],1), dtype=photo.dtype)
    return initial_layer + value

def rgb_to_rgba(photo):
    alpha_channel = solid_layer(photo)
    return np.concatenate((photo,alpha_channel), axis=2)

# TODO how to handle exceptions
# TODO make adding the alpha channel optional
def resize(photo):
   if len(photo.shape) < 3:
        print(f'''I don't know how to handle luminance data''')
        return None
   elif photo.shape[2] == 3:
        return rgb_to_rgba(photo)
   else:
        return photo

#TODO how to handle exceptions?
def prepare_data(photo):
    '''
    makes the data uint8 for use in creating the 'uint4' data
    '''
    if photo.dtype == "float32":
        return float_to_u8(photo)
    elif photo.dtype == "uint8":
        return photo
    else:
        print(f'''I don't know how to handle this number type''') 
        return None

# TODO add exception catching for bad types 
def create_u4(photo):
    data = resize(photo)
# expects uint8 input data with
    return (data/17).round().astype(np.uint8)


# TODO create deafault name for empty input
def create_preview(photo):
    uint8_data = u4_to_u8(photo)
    preview = input('Enter name of preview image relative to current directory: ')
    plt.imsave(preview, uint8_data)



# TODO add mif compression
# TODO make the mif generation quicker (compression should help)

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

# TODO ask for filname for mif data
def write_mif(photo, mode='x', file='mifData.mif'):
   '''
   this writes out the mif
   '''
   f = open(file, mode)
   f.write(form_mif(photo))
   f.close()