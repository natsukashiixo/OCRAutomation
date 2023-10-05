# this is just a reference file, some of these functions won't actually work if straight up imported into the ui
from typing import Union
import os
import math
from app.src.modules.logger_mod import write_log as WriteLog

def clicked():
    print("buttonclick")
    
def open_folder(path: Union[str, os.PathLike]):
    try:
        realpath = os.path.realpath(path)
        os.startfile(realpath)
    except Exception as e:
        WriteLog(e)
    
    
def exit_button():
    #sys.exit(app.exec_() #this probably needs to be in the actual UI file I guess
    pass

def round_seconds(seconds):
        try:
            seconds = int(seconds)
            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            return h, m, s
        except Exception as e:
            WriteLog(e)
        

class ProgressCounter:
    def __init__(self, total):
        self.total = total
        self.counter = 0
        self.previous_percent = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def update_progress(self):
        try:
            self.counter += 1
            percent_done = (self.counter / self.total) * 100
            floored_percent = math.floor(percent_done)
            if self.total < 100:
                print(f"{percent_done:.2f}% done")
            elif floored_percent%5 == 0 and floored_percent != self.previous_percent:
                self.previous_percent = floored_percent
                print(f"{percent_done:.2f}% done")
        except Exception as e:
            WriteLog(e)
        
        
    def finalize(self):
        print('Operation completed')    

if __name__ == "__main__":
    pass

    
