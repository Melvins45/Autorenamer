import sys
import os
from PySide2.QtWidgets import *
from PySide2.QtCore import (QFile, QIODevice, Signal)
from PySide2.QtUiTools import QUiLoader
import constants as gc
import re
import threading
import math
    
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
    if file_name == "home" :    
        class _Main_Window(QMainWindow):
            # compiling = [ Signal(str) for i in range(100) ]
            # compiling0 = Signal()
            # compiling1 = Signal()
            compilingAll = Signal(str)
            # self.
                        
            def __init__(self, parent=None):
                super(_Main_Window, self).__init__(parent)

                self.m_ui = gc.PAGES_UI[file_name]
                self.m_ui.setupUi(self)
        return _Main_Window()
    elif "dialog" in file_name :
        class _Window_Dialog(QDialog):
            def __init__(self, parent=None):
                super(_Window_Dialog, self).__init__(parent)

                self.m_ui = gc.PAGES_UI[file_name]
                self.m_ui.setupUi(self)
        return _Window_Dialog()
    else :
        class _Window(QWidget):
            def __init__(self, parent=None):
                super(_Window, self).__init__(parent)

                self.m_ui = gc.PAGES_UI[file_name]
                self.m_ui.setupUi(self)
        return _Window()
    
def autoWrap(_text: str, _inlineCharactersSize: int) -> str :
    """Transform a string in a multiline string according to the inline size

    Args:
        _text (str): The string to transform
        _inlineCharactersSize (int): The inline size

    Returns:
        str: The multiline string transformed
    """
    return "".join([ _text[i] if i == 0 else _text[i] if i%_inlineCharactersSize != 0 else _text[i]+'\n' for i in range(len(_text)) ])    
    
def remove_from_status_bar(_status_bar : QStatusBar, _widget : QWidget) :
    """Remove a widget from the status bar

    Args:
        _status_bar (QStatusBar): The status bar from which we remove 
        _widget (QWidget): The widget to remove
    """
    # remove it from the layout list
    _status_bar.removeWidget(_widget)
    # remove it from the gui
    _widget.setParent(None)    
    
def remove_from_layout(layout: QLayout, _index: int):
    """Remove a widget from his layout

    Args:
        layout (QLayout): The layout from which we remove 
        _index (int): The index of the widget to remove
    """
    widgetToRemove = layout.itemAt(_index).widget()
    # remove it from the layout list
    layout.removeWidget(widgetToRemove)
    # remove it from the gui
    widgetToRemove.setParent(None)
    
def clear_layout(_layout: QLayout, _listToLeave: list[int] = []):
    """Clear a layout of all its children

    Args:
        _layout (QLayout): The layout to clear
        _listToLeave (list[int]): The list of index to leave
    """
    lenght = _layout.count()
    # print( [ [i, type(_layout.itemAt(i).widget())] if i > 0 else [i, _layout.itemAt(i).widget().objectName()] for i in range(lenght) ] )
    # print( [ [i, type(_layout.itemAt(i).widget())] if _layout.itemAt(i).widget() == None else [i, _layout.itemAt(i).widget().objectName()] for i in range(lenght) ] )
    # print( type(type(lenght)) )
    # print( [ [i, type(_layout.itemAt(i).widget())] for i in range(lenght) ] ) # if type(_layout.itemAt(i).widget()) == None else [i, _layout.itemAt(i).widget().objectName()] for i in range(lenght) ] )
    for i in range(lenght) : # reversed(range(lenght)): 
        # print(i, type(_layout.itemAt(i).widget()))
        if i not in _listToLeave :
            # print(i," to remove ")
            # if _layout.itemAt(i) == None :
            #     print(i, _layout.itemAt(i), " is None ")
            #     _layout.removeItem(_layout.itemAt(i))
            #     continue
            # print(i," to remove start ")
            widgetToRemove = _layout.itemAt(0).widget()
            # remove it from the layout list
            _layout.removeWidget(widgetToRemove)
            # remove it from the gui
            if widgetToRemove != None :
                widgetToRemove.setParent(None)   

def clear_all_layout(_layout: QLayout, _listToLeave: list[int] = []):
    """Clear a layout of all its children

    Args:
        _layout (QLayout): The layout to clear
        _listToLeave (list[int]): The list of index to leave
    """
    lenght = _layout.count()
    # print( [ [i, type(_layout.itemAt(i).widget())] if _layout.itemAt(i).widget() == None else [i, _layout.itemAt(i).widget().objectName()] for i in range(lenght) ] )
    for i in reversed(range(lenght)): 
        if i not in _listToLeave :
            widgetToRemove = _layout.itemAt(i).widget()
            _layout.removeWidget(widgetToRemove)
            if widgetToRemove != None :
                widgetToRemove.setParent(None)   

def reconnect(signal, newhandler = None, oldhandler = None):
    """Connect a new slot to a signal after disconnecting others

    Args:
        signal (_type_): The signal to connect to
        newhandler (function, optional): The new slot to connect. Defaults to None.
        oldhandler (function, optional): The old slot to connect. Defaults to None.
    """    
    try:
        if oldhandler is not None:
            while True:
                signal.disconnect(oldhandler)
        else:
            signal.disconnect()
    except Exception:
        pass
    if newhandler is not None:
        signal.connect(newhandler)

def escape_before(_str_to_escape: str, _str: str) -> str :
    """Get the characters behind specified characters within a string

    Args:
        _str_to_escape (str): The string placed before the researched characters
        _str (str): The string in which we have to search

    Returns:
        str: The researched characters
    """        
    pattern_string = re.escape(_str_to_escape) + "(.*)"
    pattern = re.compile(pattern_string)
    return pattern.findall(_str)[0]

def escape_before_with_pattern(_pattern_to_escape: str, _str: str) -> str :
    """Get the characters behind a specific pattern within a string

    Args:
        _pattern_to_escape (str): The pattern to escape
        _str (str): The string to search in

    Returns:
        str: The researched characters
    """    
    _str_to_escape = re.findall( _pattern_to_escape, _str )
    return escape_before(_str_to_escape[0] if len(_str_to_escape) != 0 else '' , _str), _str_to_escape[0] if len(_str_to_escape) != 0 else ''

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

def escape_pattern(_pattern_behind: str, _pattern_ahead: str, _str: str) :
    return escape_behind_with_pattern(_pattern_behind, escape_before_with_pattern(_pattern_ahead, _str)[0])[0]

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
    return f"{_file_object['name']} S{_file_object['season']:02} EP{_file_object['episode']:02}{ ' '+str(_file_object['year']) if _file_object['year'] != None else ''}{ ' '+str(_file_object['type']).upper() if _file_object['type'] != None else ''}{_file_object['extension']}"    

def get_episode_object(_file_name: str, general: bool = False) -> dict[str:any] :
    """Construct and send an episode object from the file's name 

    Args:
        _file_name (str): The file name to compile
        general (bool) (Default to False): A bool to specify if the file name is a category name

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
        "season" : 0 if len(nums1) == 0 else 1 if len(nums1) == 1 and not general else nums1[0],
        "episode" : nums1[0] if len(nums1) == 1 else nums1[1] if len(nums1) != 0 else 1,
        "nums1" : nums1,
        "year" : None if len(year) == 0 else year[0], 
        "type" : None if len(type1) == 0 else type1[0], 
        "original" : _file_name,
        "final" : get_name_from_object({
            "name" : rowysy1,
            "season" : 0 if len(nums1) == 0 else 1 if len(nums1) == 1 and not general else nums1[0],
            "episode" : nums1[0] if len(nums1) == 1 else nums1[1] if len(nums1) != 0 else 1,
            "nums1" : nums1,
            "year" : None if len(year) == 0 else year[0], 
            "type" : None if len(type1) == 0 else type1[0], 
            "original" : _file_name,
            "extension" : _str_escaped
        } ),
        "extension" : _str_escaped
    } 
    
def set_timeout(func, sec: int) -> threading.Timer:
    """Set timeout before executing a function

    Args:
        func (function): The function to execute
        sec (int): The seconds to wait before execution
    """     
    def func_wrapper():
        # set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def count_digit(n):
    return math.floor(math.log10(n)+1)-1 if n != 0 else 1