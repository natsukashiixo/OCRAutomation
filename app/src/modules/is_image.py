import sys

imagetuple_agnostic = ('474946383761', '474946383961', 'FFD8FFDB', 'FFD8FFE000104A4649460001', 'FFD8FFEE', 'FFD8FFE1', 'FFD8FFE0', '0000000C6A5020200D0A870A', 'FF4FFF51', '89504E470D0A1A0A', '424D', ) #checks if a file is GIF, JPG, JPEG, JFIF, JPEG2000, PNG or BMP
imagetuple_little = ('49492A00', ) #checks if a file is TIFF in little endian
imagetuple_big = ('4D4D002A', ) #checks if a file is TIFF in big endian

# Determine the byte order of the CPU
if sys.byteorder == 'little':
    byteorder = 'little'
elif sys.byteorder == 'big':
    byteorder = 'big'
else:
    raise Exception("Byte order can't be determined")

def is_image(file):
    """
    Returns a boolean indicating whether the given file is an image or not.
    """
    try:
        file_bytes = open(file, 'rb').read()
        hexbytes = file_bytes.hex()
        if any(hexbytes[slice(32)].upper().startswith(pattern) for pattern in imagetuple_agnostic) or any(hexbytes[slice(32)].upper().startswith(pattern) for pattern in (imagetuple_little if byteorder == 'little' else imagetuple_big)):
            return True
        else:
            return False
    except BaseException as error:
        print('An exception occurred while processing {}: {}'.format(file, error))
        return False


#Example code by chatGPT
#from pathlib import Path
#
#root_folder = '.'
#all_files = Path(root_folder).rglob('*.*')
#
#for file in all_files:
#    if is_image(file):
#        print(file, 'is image, deleting')
        # delete the file
#    else:
#        print(file, 'is not image, skipping')
