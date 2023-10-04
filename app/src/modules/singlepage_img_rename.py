from pathlib import Path
from app.src.modules.is_image import is_image as IsImage
import os
import shutil
from app.src.modules.functions_ui import ProgressCounter
import re
from natsort import os_sorted

rootfolder = './ImportFolder'
destination = Path('./TesseractInput/')

def single_rename(rootfolder=rootfolder, destination=destination):
    allfiles = list(Path(rootfolder).rglob('*.*'))
    ImageList = []
    RenamedFiles = []
    Counter = '0001'
    has_numbers = re.compile(r'[0-9]')
    
    if all(has_numbers.search(str(file)) for file in allfiles):
        print('All images are numbered, using Windows sorting')
        ImageList = [file for file in allfiles if IsImage(file)]
        ImageList = os_sorted(ImageList)
    
    else:
        print("Images aren't ordered, ordering based on file creation date")
        try:
            for file in allfiles:
                if IsImage(file): 
                    os.path.getctime(file)
                    #print(file, 'was created at:', os.path.getctime(file), 'in UNIX time') # Read file creation time for each image file using os.path.getctime
                    ImageList.append(file)
                else:
                    print(file, "is not an image")
        except BaseException as error:
                print('An exception occurred while processing {}: {}'.format(file, error))
        ImageList = sorted(ImageList, key=os.path.getctime)

    # Rename each file sequentially using the order found in ImageList, incrementing Counter by 1 with each file read

    files = list(filter(IsImage, allfiles))

    with ProgressCounter(len(files)) as progress:
        for file in ImageList:
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