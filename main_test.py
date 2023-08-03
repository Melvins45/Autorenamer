import os
from glob import glob
from pathlib import Path
import re
import shutil
from collections import Counter
from random import randint

def shared_chars(s1, s2):
    return sum((Counter(s1) & Counter(s2)).values())

# def countDigit(n):
#     return math.floor(math.log10(n)+1)-1

start_dir = "C:\\Users\\user\\Downloads\\Telegram Desktop\\" #"G:\\cygwino\\New\\Overlord\\Overlord S2\\"
start = lambda file : start_dir+file
typeWords = ['vf', 'vostfr']
badNameWords = typeWords.copy()
badNameWords.extend(['ep','episode','s','saison','season','#new','voiranime','fin','hd','mp'])
    
# Get the rank of the actual file
def detect_rank(file : str) :
    file_name = Path(file).stem
    return int(re.findall(r'\d+', file_name)[-1]) if len(re.findall(r'\d+', file_name)) != 0 else 1 #int(re.search(r'\d+', file_name).group())+1

def capitalise_all(_string: str, _delimiter: str = " ") -> str :
    """Capitalise all substrings splitted from an original string with a delimiter

    Args:
        _string (str): The original string
        _delimiter (str, optional): The delimiter of words. Defaults to " ".

    Returns:
        str: The string resulted with all substrings capitalised
    """
    return ' '.join([ i.capitalize() for i in _string.split(_delimiter) ])    

files = os.listdir(start_dir)#glob(start("*.mp4"))
final_ep = glob(start("final ep\\*.mp4"))

def splittable(_string: str, splitters: list[str]) -> bool :
    """Test if a string is splittable by any of the members of a list of substrings

    Args:
        _string (str): The string to test if splittable
        splitters (list[str]): The list of the possible splitters

    Returns:
        bool: The test's result
    """    
    return len(list([ i for i in splitters if re.search(re.escape(i), _string) != None ])) != 0

def escape_behind(_str_to_escape: str, _str: str) -> str :
    """Get the characters before specified characters within a string

    Args:
        _str_to_escape (str): The string placed behind the researched characters
        _str (str): The string in which we have to search

    Returns:
        str: The researched characters
    """        
    pattern_string = "(.*)" + re.escape(_str_to_escape) 
    pattern = re.compile(pattern_string)
    return pattern.findall(_str)[0]

def escape_behind_with_pattern(_pattern_to_escape: str, _str: str) -> str :
    """Get the characters before a specific pattern within a string

    Args:
        _pattern_to_escape (str): The pattern to escape
        _str (str): The string to search in

    Returns:
        str: The researched characters
    """    
    _str_to_escape = re.findall( _pattern_to_escape, _str )
    return escape_behind(_str_to_escape[0] if len(_str_to_escape) != 0 else '' , _str)

def get_episode_object(_file_name: str) -> dict[str:any] :
    """Construct and send an episode object from the file's name 

    Args:
        _file_name (str): The file name to compile

    Returns:
        dict[str:any]: The resulted episode object
    """
    # print(_file_name)
    _file_namey = escape_behind_with_pattern( r'\..{1,4}$', _file_name )  
    list1 = re.findall( r'\d+', _file_namey )
    set1 = [i for n, i in enumerate(list1) if i not in list1[:n]]
    year = [ int(i) for i in set1 if int(i) > 2000 ]
    nums1 = [ int(i) for i in set1 if int(i) < 100 ]
    rowsy1 = re.findall( r'[@a-zA-Z0-9]+', _file_namey )
    row1 = [ rowsy1[i] for i in range(len(rowsy1))
            if rowsy1[i]!=''
                # and len([ j for j in badNameWords if j in i.lower() ]) == 0 
                and rowsy1[i].find('@') == -1
                and rowsy1[i].lower() not in badNameWords ]
    type1 = [ rowsy1[i] for i in range(len(rowsy1))
            if rowsy1[i].lower()  in typeWords ]
    # rowy1 = [ i for i in row1 if re.search( r'[a-zA-Z]+', i ) != None ]
    rowy1 = [i for n, i in enumerate(row1) if i not in row1[:n]]
    rowysy1 = ' '.join(rowy1)
    # print(row1)

    rowysy1 = escape_behind_with_pattern( r' [sS]\d.*$', rowysy1 )
    rowysy1 = ' '.join(re.findall( r'[a-zA-Z]+', rowysy1 ))
    # rowysy1 = escape_behind_with_pattern( r' [sS] .*$', rowysy1 )
    # rowysy1 = ' '.join(re.findall( r'[a-zA-Z]+', rowysy1 ))
    # rowysy1 = escape_behind_with_pattern( r' [eE]$', rowysy1 )
    # rowysy1 = ' '.join(re.findall( r'[a-zA-Z]+', rowysy1 ))

    return {
        "name" : rowysy1,
        "season" : 1 if len(nums1) <= 1 else nums1[0],
        "episode" : nums1[0] if len(nums1) == 1 else nums1[1] if len(nums1) != 0 else 0,
        "nums1" : nums1,
        "year" : None if len(year) == 0 else year[0], 
        "type" : None if len(type1) == 0 else type1[0], 
        "original" : _file_name
    }

#os.rename(files[0], start('Overlord S2 VF EP01.mp4'))

if __name__ == "__main__" :
    
    # Test some functions
    filesy = [ i for i in files if re.search( r'\..*$', i ) != None ]
    
    # filesy1 = escape_behind_with_pattern( r'\..{1,4}$', filesy[index] ) # '[@AnimesZone]Dr.Stone Saison 2 episode 4'
    # list1 = re.findall( r'\d+', filesy1 )
    # set1 = [i for n, i in enumerate(list1) if i not in list1[:n]]
    # year = [ int(i) for i in set1 if int(i) > 2000 ]
    # nums1 = [ int(i) for i in set1 if int(i) < 100 ]
    # rowysy1 = filesy1
    # indexSplitter = 0
    # splitters = [']',' ','_','-','.']
    # print(filesy[index], filesy1, index)
    # original_name= filesy1
    # while shared_chars(rowysy1, filesy1) == len(filesy1) or rowysy1 == '' or splittable(original_name, splitters[ indexSplitter: ]) :
        # rowsy1 = original_name.split(splitters[indexSplitter])
        # rowsy1 = [ i for i in rowsy1 if i not in splitters ]#and len([ j for j in badNameWords if j in i.lower() ]) == 0 and i.lower() not in badNameWords ]
        # rowsy1 = re.findall( r'[@a-zA-Z]+', original_name )
        # row1 = [ rowsy1[i] for i in range(len(rowsy1))
        #         if rowsy1[i]!=''
        #             # and len([ j for j in badNameWords if j in i.lower() ]) == 0 
        #             and rowsy1[i].find('@') == -1
        #             and rowsy1[i].lower() not in badNameWords ]
        # type1 = [ rowsy1[i] for i in range(len(rowsy1))
        #         if rowsy1[i].lower()  in typeWords ]
        # rowy1 = [ i for i in row1 if re.search( r'[a-zA-Z]+', i ) != None ]
        # rowy1 = [i for n, i in enumerate(rowy1) if i not in rowy1[:n]]
        # rowysy1 = ' '.join(rowy1)
        # print(original_name, rowsy1, splitters[indexSplitter:])
        # splittableFromRow = max(rowsy1, key=len) if splittable(max(rowsy1, key=len), splitters[indexSplitter:]) and len(rowsy1) < 4 else 0 #[ i for i in rowsy1 if splittable(i, splitters[indexSplitter:]) ]
        # original_name = original_name if rowsy1[0] == original_name else splittableFromRow if splittableFromRow != 0 else '' #rowsy1[0]
        # print('Second : ', original_name, splittable("@AnimesZonePremium", splitters[ indexSplitter: ]), rowsy1, splitters[indexSplitter:])
        # if indexSplitter == len(splitters)-1 :
            # break
        # indexSplitter += 1 if indexSplitter < len(splitters)-1 else 0

    
    # rowsy1 = re.findall( r'[@a-zA-Z]+', original_name )
    # row1 = [ rowsy1[i] for i in range(len(rowsy1))
    #         if rowsy1[i]!=''
    #             # and len([ j for j in badNameWords if j in i.lower() ]) == 0 
    #             and rowsy1[i].find('@') == -1
    #             and rowsy1[i].lower() not in badNameWords ]
    # type1 = [ rowsy1[i] for i in range(len(rowsy1))
    #         if rowsy1[i].lower()  in typeWords ]
    # rowy1 = [ i for i in row1 if re.search( r'[a-zA-Z]+', i ) != None ]
    # rowy1 = [i for n, i in enumerate(rowy1) if i not in rowy1[:n]]
    # rowysy1 = ' '.join(rowy1)

    # rowysy1 = escape_behind_with_pattern( r' [sS]\d', rowysy1 )
    # rowysy1 = ' '.join(re.findall( r'[a-zA-Z]+', rowysy1 ))
    # rowysy1 = escape_behind_with_pattern( r' [eE]$', rowysy1 )
    # rowysy1 = ' '.join(re.findall( r'[a-zA-Z]+', rowysy1 ))

    # fileObject1 = {
    #     "name" : rowysy1,
    #     "season" : 1 if len(nums1) == 1 else nums1[0],
    #     "episode" : nums1[0] if len(nums1) == 1 else nums1[1],
    #     "nums1" : nums1,
    #     "year" : None if len(year) == 0 else year[0], 
    #     "type" : None if len(type1) == 0 else type1[0] 
    # }
    
    # index = 137 # 125 #183 #252 #179 #146 #8
    # index = randint(0, len(filesy)-1)
    # print( get_episode_object('Overlord_4_-_02_VF.mp4') )
    # print(index, filesy[index], get_episode_object(filesy[index]))
    filesyly = [ get_episode_object(i) for i in filesy ]
    files_names = [ capitalise_all(i['name']) for i in filesyly ]
    files_names = sorted([i for n, i in enumerate(files_names) if i not in files_names[:n]])
    files_sorted = [ [ j for j in filesyly if i in capitalise_all(j["name"]) ] for i in files_names ]
    
    print(files_sorted, capitalise_all("ret rEt"))
    
    with open("console.txt", 'w', encoding='utf8') as f :
        # f.write('\n')
        # f.write(str(files_sorted))
        # f.write('\n')
        # f.write(str(files_names))
        [ f.write(str(i)+'\n') for i in files_sorted ]
    
    # print(detect_rank(files[0]))
    
    # Rename it
    """
    for file in files :
        print(file, detect_rank(file))
        os.rename( file, start("Overlord S2 VF EP "+str(detect_rank(file)).zfill(2))+".mp4" )"""
        
    # Cut and paste final ep
    #shutil.move(final_ep[0], start("Overlord S2 VF EP 12.mp4")) 
    
    # Delete dir final ep
    # os.rmdir(r'G:\3D Objects\Autorenamer\kery')
    
    # Create a new dir
    # newpath = r'G:\3D Objects\Autorenamer\kery' 
    # if not os.path.exists(newpath):
    #     os.makedirs(newpath)
    
    # Show the results
    # print(os.listdir(start_dir))