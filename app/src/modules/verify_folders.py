from pathlib import Path
import os

def verify_folder(path: str):
    folder = Path(path)
    if folder.is_dir():
        return True
    else:
        folder.mkdir()
    # this was gonna be part of refactoring but i've changed my mind

def write_folder_flag():
    if not all([
    app_folder_check(),
    asset_folder_check(),
    scan_folder_check(),
    splitter_folder_check(),
    tesseract_in_folder_check(),
    tesseract_out_folder_check()
    ]):
        return False
    else:
        with open('./flags.txt', 'a') as flag_file:
            flag_file.write('FOLDERS = 1\n')

def read_folder_flag():
    if not os.path.isfile('./flags.txt'):
        return False
    else:
        with open('./flags.txt', 'r') as f:
            flag_list = [line.rstrip('\n') for line in f]
            if 'FOLDERS = 1' in flag_list:
                return True
            else:
                return False   

def app_folder_check():
    app_folder = Path('./app')
    if app_folder.is_dir():
        #print('folder 1 exists')
        return True
    else:
        app_folder.mkdir()
        
def script_folder_check():
    src_folder = Path('./app/src')
    if src_folder.is_dir():
        #print('folder 1 exists')
        return True
    else:
        src_folder.mkdir()
    
def asset_folder_check():
    asset_folder = Path('./app/assets')
    if asset_folder.is_dir():
        #print('folder 1 exists')
        return True
    else:
        asset_folder.mkdir()    
    
def scan_folder_check():
    scan_folder = Path('./ImportFolder')
    if scan_folder.is_dir():
        #print('folder 2 exists')
        return True
    else:
        scan_folder.mkdir()
    
def splitter_folder_check():
    splitter_folder = Path('./SplitterInput')
    if splitter_folder.is_dir():
        #print('folder 3 exists')
        return True
    else:
        splitter_folder.mkdir()

def tesseract_in_folder_check():
    tesseract_in_folder = Path('./TesseractInput')
    if tesseract_in_folder.is_dir():
        #print('folder 4 exists')
        return True
    else:
        tesseract_in_folder.mkdir()
    
def tesseract_out_folder_check():
    tesseract_out_folder = Path('./TesseractOutput')
    if tesseract_out_folder.is_dir():
        #print('folder 5 exists')
        return True
    else:
        tesseract_out_folder.mkdir()
    
if __name__ == "__main__":
    app_folder_check()
    script_folder_check()
    asset_folder_check()
    scan_folder_check()
    splitter_folder_check()
    tesseract_in_folder_check()
    tesseract_out_folder_check()