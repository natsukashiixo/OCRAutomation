from pathlib import Path
import pytesseract
import cv2
from modules.is_image import is_image as IsImage
from about_time import about_time
from modules.functions_ui import round_seconds

def run_tesseract(psm_nr=3):
    
    input_dir = Path('./TesseractInput').glob('*.*')
    output_file = Path('./TesseractOutput/output.xml')
    output_pdf = Path('./TesseractOutput/output.pdf')

    #Because we're using LSTM this doesn't seem to work very well. #It's worked recently but in case the model decides to not like whitelists again, the regex corrector works as a backup guard so its fine to leave it be probably.
    
    #cfg_filename = 'letters' #a file containing the 
    # whitelist located in tessdata/configs #isnt reliable between machines. kept for posterity. 
    
    #Import path to tesseract executable
    with open('tesseract_install.txt', 'r') as file:
        install_path = file.read()

    pytesseract.pytesseract.tesseract_cmd = install_path

    files = list(filter(IsImage, input_dir))

    with about_time() as t1:
        total_iterations = len(files)
        remaining_iterations = len(files)
        completed_iterations = 0 
        print(f'Starting Tesseract using PSM {psm_nr}, there are {total_iterations} pages to read.')
        for file in files:
            print(f'Starting work on {file}')
            try: 
                img_cv = cv2.imread(str(file)) 
                img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
                hocr = pytesseract.image_to_pdf_or_hocr(img_rgb, extension='hocr', lang='swe+script/Latin', config=f"--oem 3 --psm {psm_nr}", ) #Initializes tesseract, sets output format to hOCR, sets language to swedish
                completed_iterations += 1
                average_time = t1.duration / completed_iterations
                eta = average_time * remaining_iterations
                print(f'Tesseract has been reading for {t1.duration_human}')
                h, m, s = round_seconds(eta)
                print(f'The current ETA is {h}h:{m}m:{s}s')
                avgh, avgm, avgs = round_seconds(average_time)
                print(f'Average time per page is {avgh}h:{avgm}m:{avgs}s')
                remaining_iterations -= 1
                print(f'{completed_iterations} pages complete, {remaining_iterations} pages remaining out of {total_iterations}')
                
                
                with open(output_file, 'ab') as f:
                    f.write(hocr)
                    
                    # Get a searchable PDF if the document is only one page. Mostly for debugging purposes
                    #if len(files) == 1:
                    #    with open(output_pdf, 'ab') as #pdf_file: # Open the PDF output file
                    #        pdf = pytesseract.#image_to_pdf_or_hocr(img_rgb, #extension='pdf', lang='script/Latin+swe')
                    #        pdf_file.write(pdf) # Write the PDF output to the file
            except BaseException as error:
                print('An exception occurred while processing {}: {}'.format(file, error))
    print(f'total time taken was {t1.duration_human}')
                
if __name__ == "__main__":
    run_tesseract()