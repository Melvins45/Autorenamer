import os
import glob
from pathlib import Path
import re
import shutil


start_dir = "G:\\cygwino\\New\\yamada kun and the seven witches" #"G:\\cygwino\\New\\Overlord\\Overlord S2\\"
start = lambda file : start_dir+file

# Get the rank of the actual file
def detect_rank(file : str) :
    file_name = Path(file).stem
    return int(re.findall(r'\d+', file_name)[-1]) if len(re.findall(r'\d+', file_name)) != 0 else 1 #int(re.search(r'\d+', file_name).group())+1

files = glob.glob(start("*.mp4"))
final_ep = glob.glob(start("final ep\\*.mp4"))

#os.rename(files[0], start('Overlord S2 VF EP01.mp4'))

if __name__ == "__main__" :
    
    # Test some functions
    print(os.listdir(start_dir))
    print(files)
    print(detect_rank(files[0]))
    
    # Rename it
    """
    for file in files :
        print(file, detect_rank(file))
        os.rename( file, start("Overlord S2 VF EP "+str(detect_rank(file)).zfill(2))+".mp4" )"""
        
    # Cut and paste final ep
    #shutil.move(final_ep[0], start("Overlord S2 VF EP 12.mp4")) 
    
    # Delete dir final ep
    #os.rmdir(start("final ep"))
    
    # Show the results
    print(os.listdir(start_dir))