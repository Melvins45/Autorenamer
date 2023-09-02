import sys
import os
from PySide2.QtWidgets import *
from PySide2.QtCore import (QFile, QIODevice)
from PySide2.QtUiTools import QUiLoader
import constants as gc
import re
    
def load_ui(file_name:str) -> QWidget:
    """Load an ui file in a QWidget and return it

    Args:
        file_name (str): The name of the specified ui file

    Returns:
        QWidget: The resulted QWidget
    """    
    ui_page_file = QFile(gc.PAGES[file_name])
    if not ui_page_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {file_name} : {ui_page_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_page_file)
    ui_page_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    return window  

def load_py(file_name:str) -> QWidget:
    """Load python compiled ui file in QWidget

    Args:
        file_name (str): The name of the compiled python file from ui file

    Returns:
        QWidget: The resulted QWidget
    """
    if file_name != "home" :    
        class _Window(QWidget):
            def __init__(self, parent=None):
                super(_Window, self).__init__(parent)

                self.m_ui = gc.PAGES_UI[file_name]
                self.m_ui.setupUi(self)
        return _Window()
    else :
        class _Window(QMainWindow):
            def __init__(self, parent=None):
                super(_Window, self).__init__(parent)

                self.m_ui = gc.PAGES_UI[file_name]
                self.m_ui.setupUi(self)
        return _Window()
    
def clear_layout(layout: QVBoxLayout):
    """Clear a layout of all its childrean

    Args:
        layout (QVBoxLayout): The layout to clear
    """
    for i in reversed(range(layout.count())): 
        widgetToRemove = layout.itemAt(i).widget()
        # remove it from the layout list
        layout.removeWidget(widgetToRemove)
        # remove it from the gui
        widgetToRemove.setParent(None)   

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
    return escape_behind(_str_to_escape[0] if len(_str_to_escape) != 0 else '' , _str), _str_to_escape[0] if len(_str_to_escape) != 0 else ''

def capitalise_all(_string: str, _delimiter: str = " ") -> str :
    """Capitalise all substrings splitted from an original string with a delimiter

    Args:
        _string (str): The original string
        _delimiter (str, optional): The delimiter of words. Defaults to " ".

    Returns:
        str: The string resulted with all substrings capitalised
    """
    return ' '.join([ i.capitalize() for i in _string.split(_delimiter) ])    

def get_name_from_object(_file_object: dict) -> str :
    """Get a file object and return the resulted name of the file

    Args:
        _file_object (dict): The file object to treat

    Returns:
        str: The resulted name
    """
    return f"{_file_object['name']} S{_file_object['season']:02} EP{_file_object['episode']:02}{ ' '+str(_file_object['year']) if _file_object['year'] != None else ''}{ ' '+str(_file_object['type']) if _file_object['type'] != None else ''}{_file_object['extension']}"    

def get_episode_object(_file_name: str) -> dict[str:any] :
    """Construct and send an episode object from the file's name 

    Args:
        _file_name (str): The file name to compile

    Returns:
        dict[str:any]: The resulted episode object
    """
    # print(_file_name)
    _file_namey, _str_escaped = escape_behind_with_pattern( r'\..{1,4}$', _file_name )  
    list1 = re.findall( r'\d+', _file_namey )
    set1 = [i for n, i in enumerate(list1) if i not in list1[:n]]
    year = [ int(i) for i in set1 if int(i) > 2000 ]
    nums1 = [ int(i) for i in set1 if int(i) < 100 ]
    rowsy1 = re.findall( r'[@a-zA-Z0-9]+', _file_namey )
    row1 = [ rowsy1[i] for i in range(len(rowsy1))
            if rowsy1[i]!=''
                # and len([ j for j in BAD_NAME_WORDS if j in i.lower() ]) == 0 
                and rowsy1[i].find('@') == -1
                and rowsy1[i].lower() not in gc.BAD_NAME_WORDS ]
    type1 = [ rowsy1[i] for i in range(len(rowsy1))
            if rowsy1[i].lower()  in gc.TYPE_VIDEOS ]
    # rowy1 = [ i for i in row1 if re.search( r'[a-zA-Z]+', i ) != None ]
    rowy1 = [i for n, i in enumerate(row1) if i not in row1[:n]]
    rowysy1 = ' '.join(rowy1)
    # print(row1)

    rowysy1, _str_escapedy = escape_behind_with_pattern( r' [sS]\d.*$', rowysy1 )
    rowysy1 = ' '.join(re.findall( r'[a-zA-Z]+', rowysy1 ))
    # rowysy1 = escape_behind_with_pattern( r' [sS] .*$', rowysy1 )
    # rowysy1 = ' '.join(re.findall( r'[a-zA-Z]+', rowysy1 ))
    # rowysy1 = escape_behind_with_pattern( r' [eE]$', rowysy1 )
    # rowysy1 = ' '.join(re.findall( r'[a-zA-Z]+', rowysy1 ))

    return {
        "name" : rowysy1,
        "season" : 1 if len(nums1) <= 1 else nums1[0],
        "episode" : nums1[0] if len(nums1) == 1 else nums1[1] if len(nums1) != 0 else 1,
        "nums1" : nums1,
        "year" : None if len(year) == 0 else year[0], 
        "type" : None if len(type1) == 0 else type1[0], 
        "original" : _file_name,
        "final" : get_name_from_object({
            "name" : rowysy1,
            "season" : 1 if len(nums1) <= 1 else nums1[0],
            "episode" : nums1[0] if len(nums1) == 1 else nums1[1] if len(nums1) != 0 else 1,
            "nums1" : nums1,
            "year" : None if len(year) == 0 else year[0], 
            "type" : None if len(type1) == 0 else type1[0], 
            "original" : _file_name,
            "extension" : _str_escaped
        } ),
        "extension" : _str_escaped
    } 