import docx2txt
from pathlib import Path
import re

input_file = Path('./TesseractOutput/to_be_parsed.docx')
output_file = Path('./TesseractOutput/less_mistakes.txt')

def regex_corrector(input_file=input_file, output_file=output_file):
    print('Starting regex correction of hOCR data')
    linebreak = re.compile('[a-z]- ')
    pagenumber = re.compile('(\n\d \n)|(\n\d\d \n)|(\n\d\d\d \n)')    
    stupid_french_e_l = re.compile('è')
    stupid_french_e_u = re.compile('È')

    text = docx2txt.process(input_file)

    mistakes_no = 0

    updated_text = ""

    with open(output_file, 'wt') as f:
        f.write(text)
        
    with open(output_file, 'rt') as f: #Running a loop to count the number of mistakes because I'm inefficient
        text = f.read()
        for sentence in re.split('[.]', text):
            lm = linebreak.search(sentence)
            pm = pagenumber.search(sentence)
            sfelm = stupid_french_e_l.search(sentence)
            sfeum = stupid_french_e_u.search(sentence)
            if lm:
                mistakes_no += 1
            if pm:
                mistakes_no += 1
            if sfelm:
                mistakes_no += 1
            if sfeum:
                mistakes_no += 1
            else:
                pass
        f.close()
        
        with open(output_file, 'rt') as f:
            text = f.read()
            for sentence in re.split('[.]', text): #Iterates through sentences and replaces regex matches
                lm = linebreak.search(sentence)
                pm = pagenumber.search(sentence)
                sfelm = stupid_french_e_l.search(sentence)
                sfeum = stupid_french_e_u.search(sentence)
                if lm:
                    re_match = lm.group()
                    sentence = sentence.replace('- ', '')
                if pm:
                    re_match = pm.group()
                    sentence = sentence.replace(re_match, '')
                if sfelm:
                    re_match = sfelm.group()
                    sentence = sentence.replace(re_match, 'e')
                if sfeum:
                    re_match = sfeum.group()
                    sentence = sentence.replace(re_match, 'E')
                else:
                    pass
                updated_text += sentence + "."
            f.close()
        
    with open(output_file, 'wt') as f:
        f.write(updated_text)
        f.close()    

    print(f'{mistakes_no} mistakes found and corrected')

if __name__ == "__main__":
    regex_corrector(input_file, output_file)