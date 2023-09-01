from pathlib import Path
from os.path import expandvars, abspath
import os
import urllib.request

starting_dir = abspath(Path('.'))
appdata_local = expandvars('%LOCALAPPDATA%')
tesseract_search = Path(appdata_local).rglob('./tesseract.exe')
lat_url = 'https://github.com/tesseract-ocr/tessdata_best/raw/main/script/Latin.traineddata'
swe_url = 'https://github.com/tesseract-ocr/tessdata_best/raw/main/swe.traineddata'

# Create a Path object for the Latin.traineddata file
lat_traineddata_reference = Path(appdata_local, 'Programs', 'Tesseract-OCR', 'tessdata', 'script', 'Latin.traineddata')

# Create a Path object for the swe_best traineddata file
swe_traineddata_reference = Path(appdata_local, 'Programs', 'Tesseract-OCR', 'tessdata','swe.traineddata')

# Create a Path object for the letters whitelist file file
whitelist_file_reference = Path(appdata_local, 'Programs', 'Tesseract-OCR', 'tessdata', 'configs', 'letters')

def tesspath_create():
    if Path('./tesseract_install.txt').is_file():  # Looks for a text file and trained data
        pass
    else:
        for file in tesseract_search:
            if not tesseract_search:
                print("Tesseract not found, make sure it's installed in the default folder.")
                return
            else:
                os.chdir(appdata_local)
                abspath_file = abspath(file)
                os.chdir(starting_dir)
                f = open('./tesseract_install.txt', 'a')
                f.write(abspath_file)
                f.close()
    
def tessinstall_flag():
    if Path('./tesseract_install.txt').is_file():
        return True
    else:
        return False
       
def latdata_flag():
    if not os.path.isfile('./flags.txt'):
        return False
    else:
        with open('./flags.txt', 'r') as f:
            flag_list = [line.rstrip('\n') for line in f]
            if 'LATDATA = 1' in flag_list:
                return True
            else:
                return False
    
def swedata_flag():
    if not os.path.isfile('./flags.txt'):
        return False
    else:
        with open('./flags.txt', 'r') as f:
            flag_list = [line.rstrip('\n') for line in f]
            if 'SWEDATA = 1' in flag_list:
                return True
            else:
                return False
            
            
def latdata_download():
    if not tessinstall_flag():
        print("Tesseract couldn't be found. Make sure it's installed and that ../tesseract_install.txt contains a valid path to the program file.")
        return
    
    elif latdata_flag():
        return
    
    elif os.path.isfile(lat_traineddata_reference):
        with open('./flags.txt', 'a') as flag_file:
            flag_file.write('LATDATA = 1\n')
    
    else:
        with open('./tesseract_install.txt', 'r') as f:
            tess_exe = Path(f.read())
            install_folder = tess_exe.parent
        lat_traineddata = Path(install_folder, 'tessdata', 'script', 'Latin.traineddata')
        urllib.request.urlretrieve(lat_url, lat_traineddata)
        f.close()
        with open('./flags.txt', 'a') as flag_file:
            flag_file.write('LATDATA = 1\n')

def swedata_download():
    if not tessinstall_flag():
        print("Tesseract couldn't be found. Make sure it's installed and that ../tesseract_install.txt contains a valid path to the program file.")
        return
    
    elif swedata_flag():
        return
    
    elif os.path.isfile(swe_traineddata_reference):
        with open('./flags.txt', 'a') as flag_file:
            flag_file.write('SWEDATA = 1\n')
    
    else:
        with open('./tesseract_install.txt', 'r') as f:
            tess_exe = Path(f.read())
            install_folder = tess_exe.parent
        swe_traineddata = Path(install_folder, 'tessdata', 'swe.traineddata')
        urllib.request.urlretrieve(swe_url, swe_traineddata)
        f.close()
        with open('./flags.txt', 'a') as flag_file:
            flag_file.write('SWEDATA = 1\n')

def tesseract_instructions():
    if not tessinstall_flag():
        print("Please make sure you've installed tesseract-ocr-w64 from https://github.com/UB-Mannheim/tesseract/wiki. This script assumes Tesseract was installed in",f'{appdata_local}/Programs/Tesseract-OCR. Anything else will require manual setup.')
        return
         
            
if __name__ == "__main__":
    print(f'Tessinstall flag is {tessinstall_flag()}')
    print(f'Latdata flag is {latdata_flag()}')
    print(f'Swedata flag is {swedata_flag()}')
    if not tessinstall_flag():
        print(f'Tessinstall flag is {tessinstall_flag()}')
        tesspath_create()
        tesseract_instructions()
    if not latdata_flag():
        print(f'Latdata flag is {latdata_flag()}')
        latdata_download()
    if not swedata_flag():
        print(f'Swedata flag is {swedata_flag()}')
        swedata_download()