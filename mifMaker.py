from matplotlib import image
import numpy as np
from helpers import summarize, create_u4, create_preview, write_mif, write_hex

from tempfile import TemporaryDirectory
from zipfile import ZipFile, ZIP_BZIP2
from pathlib import Path

import click
import os
from shutil import copy

def process_image(file, basedir):
        # load image as pixel array
    img = file
    data = image.imread(img)

    # create data for VGA from image array
    uint4_data = create_u4(data)

    # save converted image for preview before placing on FPGA
    create_preview(uint4_data, basedir=basedir)

    # save the data for the mif
    write_mif(uint4_data, 'w', basedir=basedir)
    write_hex(uint4_data, 'w', basedir=basedir)

@click.command()
@click.option('--input', help='Path to input image')
@click.option('--output', default='.' , help='Path to output directory')
#@click.option('--zip_out', default=1)
def create_image_package(input, output):
    # Check input for valid name

    # Create appropriate file path to access input
    current_path = Path('.')
    in_path = current_path.joinpath(input)
    out_path = current_path.joinpath(f'{output}')

    # Process image in temporary directory
    with TemporaryDirectory() as tmp_dirname:
        base_path = Path(tmp_dirname)
        file_path = base_path.joinpath(input)                              

        process_image(in_path, base_path)
        
        # creating zip and sending to client
        zip_name = f'{output}'
        zip_path = base_path.joinpath(zip_name)
        file_paths = os.listdir(base_path)

        with ZipFile(zip_path, mode="w", compression=ZIP_BZIP2, compresslevel=9) as zip:
            for file in file_paths:
                zip.write(base_path.joinpath(file), arcname=file)

        copy(zip_path, out_path)

if __name__ == '__main__':
    create_image_package()