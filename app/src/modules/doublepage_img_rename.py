from pathlib import Path
import re
from natsort import os_sorted
import os
import shutil
from app.src.modules.is_image import is_image as IsImage
from app.src.modules.functions_ui import ProgressCounter
from app.src.modules.logger_mod import write_log as WriteLog

rootfolder = './ImportFolder' 
destination = Path('./SplitterInput/')

def double_rename(rootfolder=rootfolder, destination=destination):
    try:
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
                    ext = os.path.splitext(file)[1] 
                    NewFile = os.path.join(rootfolder, f"{Counter}{ext}") 
                #print(file, 'saved as:', NewFile)
                    shutil.copy(file, NewFile) #Creates a copy of the original file with a new name and metadata
                    Counter = '{:04d}'.format(int(Counter) + 1)
                    RenamedFiles.append(NewFile)
                    progress.update_progress()
                except BaseException as error:
                    print('An exception occurred while processing {}: {}'.format(file, error))
            progress.finalize()
    
        # Move processed files to the image splitting folder
        for file in RenamedFiles:
            try:
                #print(RenamedFiles) #Debug to make sure the right file was added to this list
                #print(file, 'saved to:', destination)
                shutil.move(file, destination) 
            except BaseException as error:
                print('An exception occurred while processing {}: {}'.format(file, error))
        print(f'{len(RenamedFiles)} images renamed and moved')
    except Exception as e:
        WriteLog(e)
    

if __name__ == "__main__":
    double_rename(rootfolder, destination)