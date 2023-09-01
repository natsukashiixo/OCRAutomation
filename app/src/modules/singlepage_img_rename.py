from pathlib import Path
from modules.is_image import is_image as IsImage
import os
import shutil
from modules.functions_ui import ProgressCounter

rootfolder = './ImportFolder'
destination = Path('./TesseractInput/')

def single_rename(rootfolder=rootfolder, destination=destination):
    print('Renaming and moving files based on creation date')
    allfiles = list(Path(rootfolder).rglob('*.*'))  # Convert generator to a list
    ImageList = []
    RenamedFiles = []
    Counter = '0001'

    try:
        for file in allfiles:
            if IsImage(file):
                os.path.getctime(file)
                # print(file, 'was created at:', os.path.getctime(file), 'in UNIX time') # Read file creation time for each image file using os.path.getctime
                ImageList.append(file)
            else:
                pass
    except BaseException as error:
        print('An exception occurred while processing {}: {}'.format(file, error))

    # Rename each file sequentially using the order found in ImageList, incrementing Counter by 1 with each file read

    files = list(filter(IsImage, allfiles))

    with ProgressCounter(len(files)) as progress:
        for file in sorted(ImageList, key=os.path.getctime):
            try:
            #print(file, os.path.getctime(file)) #Debug statement
                ext = os.path.splitext(file)[1] # Save the file extension
                NewFile = os.path.join(rootfolder, f"{Counter}{ext}") # Construct the new file path
            #print(file, 'saved as:', NewFile)
                shutil.copy(file, NewFile) #Creates a copy of the original file with a new name and metadata
                Counter = '{:04d}'.format(int(Counter) + 1)
                RenamedFiles.append(NewFile)
                progress.update_progress()
            except BaseException as error:
                print('An exception occurred while processing {}: {}'.format(file, error))
        progress.finalize()
        
    # Move processed files to OCR handling folder
    for file in RenamedFiles:
        try:
            #print(RenamedFiles) #Debug to make sure the right file was added to this list
            #print(file, 'saved to:', Destination)
            shutil.move(file, destination) #Moves processed files to output folder
        except BaseException as error:
            print('An exception occurred while processing {}: {}'.format(file, error))
    print(f'{len(RenamedFiles)} images renamed and moved')
            
if __name__ == "__main__":
    single_rename(rootfolder, destination)