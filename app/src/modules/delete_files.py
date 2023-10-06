import os
from pathlib import Path
from modules.is_image import is_image as IsImage
from modules.logger_mod import write_log as WriteLog

rootfolder = './'
txt_file = Path('./TesseractOutput/less_mistakes.txt')
docx_file = Path('./TesseractOutput/to_be_parsed.docx')

def delete_irrelevant_files(rootfolder=rootfolder, txt_file=txt_file, docx_file=docx_file):
    try:
        if txt_file.is_file():
            txt_file.unlink(missing_ok=True)
        if docx_file.is_file():
            docx_file.unlink(missing_ok=True)
        # Create a list of all visible files
        allfiles = []
        excluded_folders = {'.', 'assets', '__'}
        for foldername, subfolders, filenames in os.walk(rootfolder):
            subfolders[:] = [subfolder for subfolder in subfolders if not subfolder.startswith(tuple(excluded_folders))]
            for filename in filenames:
                #print(f'cwd is {foldername}') # debug statement
                if not filename.startswith('.'):
                    allfiles.append(Path(foldername) / filename)
        for file in allfiles:
            if IsImage(file):
                Path.unlink(file)
            if str(file).endswith('.xml'):
                Path.unlink(file)
                    
        print('Images and hOCR data deleted.')
    except Exception as e:
        WriteLog(e)
    
    
if __name__ == "__main__":
    delete_irrelevant_files(rootfolder, txt_file, docx_file)