import os
import cv2
import time
from pathlib import Path
from app.src.modules.is_image import is_image as IsImage
from app.src.modules.functions_ui import ProgressCounter

# Set the path to the root directory containing the folder with images
rootfolder = './SplitterInput'


# Set the path to the directory where the split images will be saved
output_dir = Path("./TesseractInput")

def rotate_and_split_image(rootfolder=rootfolder, output_dir=output_dir):
    allfiles = list(Path(rootfolder).rglob('*.*'))
    # Initialize the counter for the split images
    counter = '0001'

    files = list(filter(IsImage, allfiles)) #Creates a list of all image files
    print(f'Starting handling of double page images, there are {len(files)} images to process')
    with ProgressCounter(len(files)) as progress:
        for file in files: #Iterates through files in the list of images
            try:
                img = cv2.imread(str(file))
                #print(file, 'loaded')
                # Check if the height is greater than the width
                if img.shape[0] > img.shape[1]:
                    # Rotate the image 90 degrees clockwise
                    img_rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
                    #print(file, 'rotated 90 degrees clockwise')
                    # Get the width and height of the rotated image
                    height, width = img_rotated.shape[:2]

                    # Split the rotated image at the middle pixel of the width
                    img_left = img_rotated[:, :width // 2]
                    img_right = img_rotated[:, width // 2:]
                    #print(file, 'split into two images')
                    # Save the split images
                    cv2.imwrite(os.path.join(output_dir, f'{counter}.jpg'), img_left)
                    #print(file, 'saved as ' f'{counter}.jpg')
                    counter = '{:04d}'.format(int(counter) + 1)
                    time.sleep(0.001)
                    cv2.imwrite(os.path.join(output_dir, f'{counter}.jpg'), img_right)
                    #print(file, 'saved as ' f'{counter}.jpg')
                    counter = '{:04d}'.format(int(counter) + 1)
                    
                    
                elif img.shape[0] < img.shape[1]:
                    #This is supposed to handle files in the proper orientation
                    height, width = img.shape[:2]
                    # Split the image at the middle pixel of the width
                    img_left = img[:, :width // 2]
                    img_right = img[:, width // 2:]
                    #print(file, ' split into two images')
                    # Save the split images
                    cv2.imwrite(os.path.join(output_dir, f'{counter}.jpg'), img_left)
                    #print(file, 'saved as ' f'{counter}.jpg')
                    counter = '{:04d}'.format(int(counter) + 1)
                    time.sleep(0.001)
                    cv2.imwrite(os.path.join(output_dir, f'{counter}.jpg'), img_right)
                    #print(file, 'saved as ' f'{counter}.jpg')
                    counter = '{:04d}'.format(int(counter) + 1)
                progress.update_progress()            
            except BaseException as error:
                print('Error in initial loop.', 'An exception occurred while processing {}: {}'.format(file, error))
        else:
            pass
    progress.finalize()

    # I'll probably never need to think about square images right? So its fine if it does nothing.
    
    if __name__ == "__main__":
        rotate_and_split_image(rootfolder, output_dir)