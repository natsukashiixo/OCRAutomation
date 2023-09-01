# This file should probably be deleted later once the GUI works.

import sys

#import functions
import modules.setup_functions
import modules.verify_folders
import modules.singlepage_img_rename
import modules.doublepage_img_rename
import modules.rotate_and_split_image
import modules.run_tesseract
import modules.hocr_parser
import modules.fix_mistakes
import modules.rewrite_docx
import modules.delete_files

# Define the maximum buffer size in bytes
MAX_BUFFER_SIZE = 1

# Ask the user to input which set of scripts to run
print('Are your scanned images double-sided? (y/n)')
while True:
    try:
        # Read user input with a maximum size of MAX_BUFFER_SIZE bytes
        user_input = sys.stdin.readline(MAX_BUFFER_SIZE).strip()

        # Validate the user input
        if user_input.lower() not in ('y', 'n', 'd'):
            raise ValueError('Invalid input! Please enter either "y" or "n". Press CRTL+C to exit')

        # If user input is valid, break out of the loop
        break

    except ValueError as e:
        print(e)

# Check the user's input and select the appropriate script set
if user_input.lower() == 'y':
    doublepage_img_rename.double_rename()
    rotate_and_split_image.rotate_and_split_image()
    run_tesseract.run_tesseract()
    hocr_parser.parse_hocr()
    fix_mistakes.regex_corrector()
    rewrite_docx.rewrite_docx()
    delete_files.delete_irrelevant_files()
elif user_input.lower() == 'n':
    singlepage_img_rename.single_rename()
    run_tesseract.run_tesseract()
    hocr_parser.parse_hocr()
    fix_mistakes.regex_corrector()
    rewrite_docx.rewrite_docx()
    delete_files.delete_irrelevant_files()
else:
    singlepage_img_rename.single_rename()
    run_tesseract.run_tesseract()
    hocr_parser.parse_hocr()
    fix_mistakes.regex_corrector()
    rewrite_docx.rewrite_docx()
