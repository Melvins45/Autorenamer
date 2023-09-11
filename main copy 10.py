from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QFile, QTextStream, QIODevice, Signal, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QMovie, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QResizeEvent)
from PySide2.QtWidgets import *
import sys, os, re
import constants as gc
import helpers as gf
import sys
import os
import win32com.client
from operator import itemgetter
import time
from enum import Enum
import Action

class CategoriesStatus(Enum) :
    NOT_TREATED = 0
    TREATED = 1

class CategoriesColors(Enum) :
    GREEN = ["rgb(28,255,81)", "rgb(126,255,152)"]
    GRAY = ["rgb(217,217,217)", "rgb(241,241,241)"]

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

actualPage = list(gc.PAGES_TITLES.keys())[0]

oShell = win32com.client.Dispatch("Wscript.Shell")
pathToMyDocuments = oShell.SpecialFolders("MyDocuments")

if __name__ == "__main__":
    # pathFolder = ""
    
    styleSheetFile = QFile( resource_path("style.qss") )
    styleSheetFile.open(QIODevice.ReadOnly)
    styleSheet = QTextStream(styleSheetFile).readAll()
    form = QApplication(sys.argv)
    fontDatabase = QFontDatabase()
    fontDatabase.addApplicationFont(resource_path("fonts\\inder.ttf"))
    form.setFont(QFont(fontDatabase.applicationFontFamilies(0)[0], 10))
    form.setStyleSheet(styleSheet)
    pathFolderLabel = QLabel()
    window = gf.load_py("home") #ClassWindow() #gf.load_ui("window")
    #window.setWindowTitle( QCoreApplication.translate("Template", "Template", None) )
    
    # Global Variables 
    window.__setattr__("pathFolder", "")
    window.__setattr__("filesNames", [])
    window.__setattr__("filesObjects", [])
    window.__setattr__("filesObjects", [])
    # window.__setattr__("filesOriginals", )
    window.__setattr__("previousDatas", {
        "filesNames" : [ ],
        "filesObjects" : [ ],
        "filesOriginalsNames" : [ ],
        "filesOriginalsObjects" : [ ],
        "canCreateNewFolder" : [ ],
        "createNewFolder" : [ ],
        "categoriesStatus" : [ ],
    })
    window.__setattr__("userActions", [])
    window.__setattr__("filesPreviousNames", [])
    window.__setattr__("filesPreviousObjects", [])
    window.__setattr__("filesPreviousOriginalsNames", [])
    window.__setattr__("filesPreviousOriginalsObjects", [])
    window.__setattr__("filesOriginalsNames", [])
    window.__setattr__("filesOriginalsObjects", [])
    window.__setattr__("categoriesNamesInputs", [])
    window.__setattr__("categoryInputs", [])
    window.__setattr__("canCreateNewFolder", [])
    # window.__setattr__("originalsCanCreateNewFolder", [])
    window.__setattr__("previousCanCreateNewFolder", [])
    # window.__setattr__("categoryInputsLabels", [])
    window.__setattr__("categoriesStatus", [])
    window.__setattr__("undoIndex", -1)
    
    def activePage(page: str) :
        match page :
            case "template" :
                print(window.__getattribute__(page).m_ui.plainTextEdit.toPlainText())
            case _ :
                print(window.__getattribute__(page).m_ui.plainTextEdit.toPlainText())
    
    def compileFiles(_pathFolder: str) -> list[list[dict]] :
        """Take a folder and return an organised list of its videos

        Args:
            _pathFolder (str): The path to the folder to organise

        Returns:
            list[dict]: The organised list of its videos
        """
        # window.__setattr__("loader", QMovie(":/loadSpinner/images/rollingSpinner.gif"))
        # window.renamer.m_ui.loader.setMovie(window.loader) 
        # window.loader.start()
        # gf.set_timeout(lambda : window.m_ui.statusbar.addWidget(window.renamer.m_ui.loadSpinner), 0)
        
        files = os.listdir(_pathFolder)
        filesy = [ i for i in files if re.search( r'\..*$', i ) != None ]
        filesyly = [ gf.get_episode_object(i) for i in filesy ]
        files_names = [ gf.capitalise_all(i['name']) for i in filesyly ]
        files_names = sorted([i for n, i in enumerate(files_names) if i not in files_names[:n]])
        files_sorted = [ [ j for j in filesyly if i in gf.capitalise_all(j["name"]) ] for i in files_names ]
        files_sorted = [ sorted(i, key=itemgetter('episode')) for i in files_sorted ]
        
        # Put the resulted objects in a state
        if len(window.filesNames) != 0 :
            window.undoIndex = -1
            window.userActions.append(Action.Action(Action.TypeActions["BROWSE"], -1, None, {
                "pathFolder" : window.pathFolder,
                "filesNames" : window.filesNames.copy(),
                "filesObjects" : window.filesObjects.copy(),
                "filesOriginalsNames" : window.filesOriginalsNames.copy(),
                "filesOriginalsObjects" : window.filesOriginalsObjects.copy(),
                "canCreateNewFolder" : window.canCreateNewFolder.copy(),
                "categoriesStatus" : window.categoriesStatus.copy(),
            } ))
        window.pathFolder = _pathFolder
        window.pathFolder = window.pathFolder.replace('/','\\')
        window.filesNames = files_names.copy()
        window.filesObjects = files_sorted.copy()
        window.filesOriginalsNames = window.filesNames.copy()
        window.filesOriginalsObjects = window.filesObjects.copy()
        window.canCreateNewFolder = [ False for i in files_names ]
        window.categoriesStatus = [ CategoriesStatus.NOT_TREATED.value for i in files_names ]
        # window.originalsCanCreateNewFolder = [ False for i in files_names ]
        
        show_categories(files_names, files_sorted)   
        # print(gf.get_name_from_object(files_sorted[0][0]))
        # print( gf.get_episode_object(gf.get_name_from_object(files_sorted[0][0])) )
        return files_sorted
        
    def show_categories(_files_names: list[str], _files_sorted: list[list[dict]]) :
        """Show in the GUI the sorted files

        Args:
            _files_names (list[str]): The names of categories
            _files_sorted (list[list[dict]]): The sorted files to show
        """
        # return
        window.categoriesNamesInputs = [ QLineEdit(i) for i in _files_names ] # _files_names.copy()
        window.categoryInputs = [ [ QLineEdit(j["final"]) for j in i ] for i in _files_sorted ]
        gf.clear_layout(window.m_ui.scrollLayout)
        [ show_category(i) for i in range(len(_files_names)) ]
            
        connect_all_widgets()
        
    def show_category(_index : int) :
        """Show the category 

        Args:
            _index (int): The index of the category to show
        """
        window.__setattr__(f"category{_index}", gf.load_py("renamer"))
        window.__setattr__(f"categoryLayout{_index}", QVBoxLayout())
        window.__getattribute__(f"categoryLayout{_index}").setObjectName(f"categoryLayout{_index}")
        for j in range(len(window.filesObjects[_index])) :
            window.__setattr__(f"category{_index}-{j}", gf.load_py("renamer"))
            if j%2 == 0 :
                window.__getattribute__(f"category{_index}-{j}").m_ui.evenOldName.setText(window.filesOriginalsObjects[_index][j]['original'])
                window.__getattribute__(f"category{_index}-{j}").m_ui.evenNewName.setText(window.filesObjects[_index][j]['final'])
                window.__getattribute__(f"category{_index}-{j}").m_ui.evenContainer.setObjectName(f"inputContainer{j}")
                window.__getattribute__(f"category{_index}-{j}").m_ui.evenNewName.setObjectName(f"inputName")
                window.__getattribute__(f"categoryLayout{_index}").addWidget(window.__getattribute__(f"category{_index}-{j}").m_ui.evenContainer)
            else :
                window.__getattribute__(f"category{_index}-{j}").m_ui.oddOldName.setText(window.filesOriginalsObjects[_index][j]['original'])
                window.__getattribute__(f"category{_index}-{j}").m_ui.oddNewName.setText(window.filesObjects[_index][j]['final'])
                window.__getattribute__(f"category{_index}-{j}").m_ui.oddContainer.setObjectName(f"inputContainer{j}")
                window.__getattribute__(f"category{_index}-{j}").m_ui.oddNewName.setObjectName(f"inputName")
                window.__getattribute__(f"categoryLayout{_index}").addWidget(window.__getattribute__(f"category{_index}-{j}").m_ui.oddContainer) 
        window.__getattribute__(f'category{_index}').m_ui.categoryLayout.addLayout(window.__getattribute__(f'categoryLayout{_index}'))
        window.__getattribute__(f"category{_index}").m_ui.category.setText(window.filesNames[_index])
        window.m_ui.scrollLayout.addWidget(window.__getattribute__(f'category{_index}').m_ui.categoryGroup)        
        
    def refresh_category(_index : int) :
        """Refresh a category

        Args:
            _index (int): The index of the category to show
        """
        # window.__setattr__(f"category{_index}", gf.load_py("renamer"))
        # gf.c
        # print(window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").children())
        gf.clear_layout(window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QVBoxLayout,"categoryLayout"), [0])
        [ window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QWidget, f"inputContainer{j}").deleteLater() for j in range(len(window.filesObjects[_index])) if window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QWidget, f"inputContainer{j}") != None ]
        # return
        window.__setattr__(f"categoryLayout{_index}", QVBoxLayout())
        window.__getattribute__(f"categoryLayout{_index}").setObjectName(f"categoryLayout{_index}")
        for j in range(len(window.filesObjects[_index])) :
            window.__setattr__(f"category{_index}-{j}", gf.load_py("renamer"))
            if j%2 == 0 :
                window.__getattribute__(f"category{_index}-{j}").m_ui.evenOldName.setText(window.filesOriginalsObjects[_index][j]['original'])
                window.__getattribute__(f"category{_index}-{j}").m_ui.evenNewName.setText(window.filesObjects[_index][j]['final'])
                window.__getattribute__(f"category{_index}-{j}").m_ui.evenContainer.setObjectName(f"inputContainer{j}")
                window.__getattribute__(f"category{_index}-{j}").m_ui.evenNewName.setObjectName(f"inputName")
                window.__getattribute__(f"categoryLayout{_index}").addWidget(window.__getattribute__(f"category{_index}-{j}").m_ui.evenContainer)
            else :
                window.__getattribute__(f"category{_index}-{j}").m_ui.oddOldName.setText(window.filesOriginalsObjects[_index][j]['original'])
                window.__getattribute__(f"category{_index}-{j}").m_ui.oddNewName.setText(window.filesObjects[_index][j]['final'])
                window.__getattribute__(f"category{_index}-{j}").m_ui.oddContainer.setObjectName(f"inputContainer{j}")
                window.__getattribute__(f"category{_index}-{j}").m_ui.oddNewName.setObjectName(f"inputName")
                window.__getattribute__(f"categoryLayout{_index}").addWidget(window.__getattribute__(f"category{_index}-{j}").m_ui.oddContainer) 
        window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QVBoxLayout,"categoryLayout").addLayout(window.__getattribute__(f'categoryLayout{_index}'))
        # window.__getattribute__(f"category{_index}").m_ui.category.setText(window.filesNames[_index])
        # window.m_ui.scrollLayout.addWidget(window.__getattribute__(f'category{_index}').m_ui.categoryGroup)   
        recolor_category(_index, "GRAY")
        
    def set_in_2D_list(_list: list, _first_index : int, _second_index : int, _value : any) :
        """Set the value at the index in a specific list of window

        Args:
            _list (list): The name of the list in window
            _first_index (int): The first index in the first dimension
            _second_index (int): The second index in the second dimension
            _value (any): The value to set
        """
        window.__getattribute__(_list)[_first_index][_second_index] = _value
        
    def set_in_2D_dict(_list: list, _first_index : int, _second_index : int, _key : any, _value : any) :
        """Set the value at the index in a specific 2D list of dictionaries of window

        Args:
            _list (list): The name of the list in window
            _first_index (int): The first index in the first dimension
            _second_index (int): The second index in the second dimension
            _key (any): The key to set
            _value (any): The value to set
        """
        window.__getattribute__(_list)[_first_index][_second_index][_key] = _value
        
    def set_in_list(_list: list, _index : int, _value : any) :
        """Set the value at the index in a specific list of window

        Args:
            _list (list): The name of the list in window
            _index (int): The index where to set
            _value (any): The value to set
        """
        window.__getattribute__(_list)[_index] = _value        
        
    def should_create_new_folder(_bool : bool, _index : int) :
        
        # Saving previous datas
        window.undoIndex = -1
        window.userActions.append(Action.Action(Action.TypeActions["CHECK_CAN_CREATE_NEW_FOLDER"], _index, _bool, window.canCreateNewFolder.copy()))
        # window.previousDatas["canCreateNewFolder"].append(Action.Action(Action.TypeActions["CHECK_CAN_CREATE_NEW_FOLDER"], _index, _bool, window.canCreateNewFolder))
        # window.previousCanCreateNewFolder.append(window.canCreateNewFolder)
        
        # Updating new datas
        window.canCreateNewFolder[_index] = _bool
        
    def create_new_folder(_first_index : int, _second_index : int) :
        """Create a new folder and paste a file in

        Args:
            _first_index (int): The first index of the file object
            _second_index (int): The second index of the file object
        """       
        # Saving previous datas
        window.undoIndex = -1
        window.userActions.append(Action.Action(Action.TypeActions["CREATE_NEW_FOLDER"], _first_index, window.filesNames[_first_index], window.categoriesStatus.copy()))
         
        if not os.path.exists(os.path.join(window.pathFolder, window.filesNames[_first_index])) :
            os.makedirs(os.path.join(window.pathFolder, window.filesNames[_first_index]))
        os.rename( os.path.join(window.pathFolder, window.filesOriginalsObjects[_first_index][_second_index]["original"]), os.path.join(os.path.join(window.pathFolder, window.filesNames[_first_index]), window.filesObjects[_first_index][_second_index]["final"]) )
        
    def recolor_category(_index : int, _color : str = "GREEN") :
        
        window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").setStyleSheet( window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").styleSheet() + f"background-color : {CategoriesColors[_color.upper()].value[0]};" )
        window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"category").setStyleSheet( window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"category").styleSheet() + f"background-color : {CategoriesColors[_color.upper()].value[0]};" )
        window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"close").setStyleSheet( window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"close").styleSheet() + f"background-color : {CategoriesColors[_color.upper()].value[0]};" )
        
        [ window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget, "categoryEntity").findChild(QWidget, f"inputContainer{j}").setStyleSheet( window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget, "categoryEntity").findChild(QWidget, f"inputContainer{j}").styleSheet() + (f"background-color : {CategoriesColors[_color.upper()].value[1]};" if j%2 == 0 else "") ) for j in range(len(window.filesObjects[_index])) ]
        
        window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"refresh").setStyleSheet( window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"refresh").styleSheet() + f"background-color : {CategoriesColors[_color.upper()].value[1]};" )
        window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"renameAll").setStyleSheet( window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"renameAll").styleSheet() + f"background-color : {CategoriesColors[_color.upper()].value[1]};" )
        window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"fuseWith").setStyleSheet( window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"fuseWith").styleSheet() + f"background-color : {CategoriesColors[_color.upper()].value[1]};" )
        
    def rename_all(_index : int) :
        # os.path.join()
        # print(os.listdir(window.pathFolder))
        # print(window.filesOriginalsObjects[_index])
        # [ print( window.filesOriginalsObjects[_index][j]["original"], window.filesObjects[_index][j]["final"] ) for j in range(len(window.filesObjects[_index])) ]
        
        # Saving previous datas
        if not window.canCreateNewFolder[_index] :
            window.undoIndex = -1
            window.userActions.append(Action.Action(Action.TypeActions["RENAME_ALL"], _index, None, window.categoriesStatus.copy()))
        
        [ os.rename( os.path.join(window.pathFolder, window.filesOriginalsObjects[_index][j]["original"]), os.path.join(window.pathFolder, window.filesObjects[_index][j]["final"]) ) if not window.canCreateNewFolder[_index] else create_new_folder(_index, j) for j in range(len(window.filesObjects[_index])) ]
        window.categoriesStatus[_index] = CategoriesStatus.TREATED.value
        recolor_category(_index)
        
        # [ shutil.move( os.path.join(window.pathFolder.replace('/','\\'), window.filesOriginalsObjects[_index][j]["original"]), os.path.join(window.pathFolder.replace('/','\\'), window.filesObjects[_index][j]["final"]) ) for j in range(len(window.filesObjects[_index])) ]
        # [ shutil.move( os.path.join(window.pathFolder, window.filesOriginalsObjects[_index][j]["original"]), os.path.join(window.pathFolder, window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget, "categoryEntity").findChild(QWidget, f"inputContainer{j}").findChild(QWidget, "inputName").text()) ) for j in range(len(window.filesObjects[_index])) ]
        
    def connect_all_widgets():
        """Connect all the widgets of the scrollLayout
        """        
        # QLineEdit.textChanged.
        [ gf.reconnect(window.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"category").textChanged, lambda _=0, i=i : window.categoriesNamesInputs[i].setText(_) ) for i in range(len(window.filesNames)) ]
        
        [  [ gf.reconnect(window.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget, "categoryEntity").findChild(QWidget, f"inputContainer{j}").findChild(QWidget, "inputName").textChanged, lambda _=0, i=i : set_in_2D_dict("filesObjects", i, j, "final", _) ) for j in range(len(window.filesObjects[i])) ] for i in range(len(window.filesNames))  ]
        
        [ gf.reconnect(window.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"refresh").clicked, lambda _=0, i=i : refresh_data(i)) for i in range(len(window.filesNames)) ]
        [ gf.reconnect(window.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"renameAll").clicked, lambda _=0, i=i : rename_all(i)) for i in range(len(window.filesNames)) ]
        [ gf.reconnect(window.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"fuseWith").clicked, lambda _=0, i=i : fuse_with(i)) for i in range(len(window.filesNames)) ]
        [ gf.reconnect(window.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"createNewFolder").toggled, lambda _, i=i : should_create_new_folder(_,i)) for i in range(len(window.filesNames)) ]
        [ gf.reconnect(window.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"close").clicked, lambda _=0, i=i : close_group(i)) for i in range(len(window.filesNames)) ]
                
    def set_in_dict(_dict : list[dict], _key : str, _value : any) :
        """Set a key, value in a dictionary

        Args:
            _dict (list[dict]): The dictionary where to set
            _key (str): The key to set
            _value (any): The value to put
        """
        _dict[_key] = _value        
                
    def fuse_categories(_where : int, _who : int) :
        """Fuse a categorie with another

        Args:
            _where (int): The category where we put the other
            _who (int): The category to put in another
        """
        if _where == None :
            # print(_where, _who)
            window.fuser.close()
            return
        # print(_where, _who)
        
        # Saving the previous data
        window.undoIndex = -1
        window.userActions.append(Action.Action(Action.TypeActions["FUSE_WITH"], _where, _who, {
            "filesNames" : window.filesNames.copy(),
            "filesObjects" : window.filesObjects.copy(),
            "filesOriginalsNames" : window.filesOriginalsNames.copy(),
            "filesOriginalsObjects" : window.filesOriginalsObjects.copy(),
        }))
        window.filesPreviousNames.append(window.filesNames.copy())
        window.filesPreviousObjects.append(window.filesObjects.copy())
        window.filesPreviousOriginalsNames.append(window.filesOriginalsNames.copy())
        window.filesPreviousOriginalsObjects.append(window.filesOriginalsObjects.copy())
        
        # Copying the datas of the _who cateory in the _where category
        window.filesObjects[_where].extend(window.filesObjects[_who])        
        window.filesObjects[_where] = sorted(window.filesObjects[_where], key=itemgetter('episode'))
        window.filesOriginalsObjects[_where].extend(window.filesOriginalsObjects[_who])        
        window.filesOriginalsObjects[_where] = sorted(window.filesOriginalsObjects[_where], key=itemgetter('episode'))
        res = []
        [ res.append(x) for x in window.filesOriginalsObjects[_where] if x not in res ]
        window.filesOriginalsObjects[_where] = res.copy()

        # Finish with the remaining tasks
        refresh_category(_where)
        close_group(_who)
        window.fuser.close()
                
    def fuse_with(_index : int) :
        """Open a popup widget to pick a category to fuse the given one in

        Args:
            _index (int): The index of the category to fuse in another
        """        
        window.__setattr__('fuser', gf.load_py('fuser'))
        window.fuser.setFont(QFont(fontDatabase.applicationFontFamilies(0)[0], 10))
        radios = []
        for i in range(len(window.filesObjects)) :
            if i != _index :
                window.__setattr__(f"fuser{i}", gf.load_py('renamer'))
                window.__getattribute__(f"fuser{i}").m_ui.categoryRadio.setText(gf.autoWrap(window.filesNames[i], 80))
                window.__getattribute__(f"fuser{i}").m_ui.categoryRadio.toggled.connect(lambda _, i=i : radios.append( i ) if _ == True else None) # set_in_dict(radios, window.filesNames[i], _)) # print(window.filesNames[i], _))
                window.fuser.m_ui.scrollLayout.addWidget(window.__getattribute__(f"fuser{i}").m_ui.categoryRadio)
        window.fuser.m_ui.ok.clicked.connect(lambda _='t' : fuse_categories(radios[-1] if len(radios) != 0 else None, _index))
        # window.fuser.m_ui.ok.clicked.connect(lambda _='t', _where = radios[i] if len(radios) != 0 else None : fuse_categories(_where, _index))
        window.fuser.show()
        # window.fuser.m_ui.scr
        # window.fuser.close()
        # QRadioButton.setText
        # QWidget.
        
    def close_group(_index : int) :
        """Close and delete a category

        Args:
            _index (int): The index of the category
        """        
        # Saving the previous datas
        window.undoIndex = -1
        window.userActions.append(Action.Action(Action.TypeActions["CLOSE_GROUP"], _index, None, {
            "filesNames" : window.filesNames.copy(),
            "filesObjects" : window.filesObjects.copy(),
            "filesOriginalsNames" : window.filesOriginalsNames.copy(),
            "filesOriginalsObjects" : window.filesOriginalsObjects.copy(),
            "canCreateNewFolder" : window.canCreateNewFolder.copy(),
            "categoriesStatus" : window.categoriesStatus.copy(),
            "categoriesNamesInputs" : window.categoriesNamesInputs.copy()
        }))
        window.filesPreviousNames.append(window.filesNames.copy())
        window.filesPreviousObjects.append(window.filesObjects.copy())
        window.filesPreviousOriginalsNames.append(window.filesOriginalsNames.copy())
        window.filesPreviousOriginalsObjects.append(window.filesOriginalsObjects.copy())
        window.previousCanCreateNewFolder.append(window.canCreateNewFolder.copy())
        # window.previousOriginalsCanCreateNewFolder.append(window.previousOriginalsCanCreateNewFolder.copy())
        
        # Delete the index of category to close
        # print(_index, len(window.filesNames)-1)
        del window.filesNames[_index]
        del window.filesObjects[_index]
        del window.filesOriginalsNames[_index]
        del window.filesOriginalsObjects[_index]
        del window.categoriesNamesInputs[_index]
        del window.categoryInputs[_index]
        del window.canCreateNewFolder[_index]
        del window.categoriesStatus[_index]
        # del window.originalsCanCreateNewFolder[_index]
        # print("After ", _index, len(window.filesNames)-1)
        
        # Remove it from layout
        gf.remove_from_layout(window.m_ui.scrollLayout, _index)
        
        # Reconnect all widgets
        connect_all_widgets()
        
    def undo() :
        match window.userActions[window.undoIndex].type.name :
            case "RENAME_ALL" :
                s = 2
        
        
    def redo() :
        if False :
            print('no')
        
        
        
    def refresh_data(_index : int) :
        """Refresh the datas of the indexed category

        Args:
            _index (int): The index of the category in the whole list
        """        
        # print(_index, window.categoryInputs[_index][0].text())
        # widget = window.m_ui.scrollLayout.itemAt(_index).widget()
        # print(widget.findChild(QWidget, "categoryEntity").findChild(QWidget, "inputContainer0").children())
        # print(widget.findChild(QWidget, "categoryEntity").findChild(QWidget, "categoryContainer").children())
        # print(widget.children()) #.findChild(QWidget, "inputContainer0").children())
        # print(widget.findChild(QWidget, "categoryEntity").children()) #.findChild(QWidget, "inputContainer0").children())
        # for i in range(window.m_ui.scrollLayout.count()): 
        # for i in reversed(range(window.__getattribute__(f'category{_index}').m_ui.categoryLayout.count())): 
            # widgetToRemove = window.m_ui.scrollLayout.itemAt(i).widget()
            # print(widgetToRemove.findChild(QWidget, "categoryEntity").children())
                #   categoryEntity.categoryContainer.category.text())
            # QWidget.fi
            # print(type( widgetToRemove))
        
        # print(_index, window.filesObjects[_index])
        if window.filesNames[_index] != window.categoriesNamesInputs[_index].text() :
            # Saving the action
            window.userActions.append(Action.Action(Action.TypeActions["REFRESH"], _index, window.categoriesNamesInputs[_index].text(), {
                "filesNames" : window.filesNames.copy(),
                "filesObjects" : window.filesObjects.copy()
            }))
            
            categoryObject = gf.get_episode_object(window.categoriesNamesInputs[_index].text(), True)
            window.filesPreviousNames.append(window.filesNames.copy())
            window.filesPreviousObjects.append(window.filesObjects.copy())
            set_in_list("filesNames", _index, window.categoriesNamesInputs[_index].text())
            # set_in_list("filesNames", _index, categoryObject["name"])
            window.__setattr__(f"categoryLayout{_index}", QVBoxLayout())
            window.__getattribute__(f"categoryLayout{_index}").setObjectName(f"categoryLayout{_index}")
            for j in range(len(window.filesObjects[_index])) :
                fileObject = window.filesObjects[_index][j] # gf.get_episode_object(window.categoryInputs[_index][j].text())
                fileObject["name"] = categoryObject["name"]
                if categoryObject["season"] != 0 :
                    fileObject["season"] = categoryObject["season"]
                if categoryObject["year"] != None :
                    fileObject["year"] = categoryObject["year"]
                if categoryObject["type"] != 0 :
                    fileObject["type"] = categoryObject["type"]
                fileObject["final"] = gf.get_name_from_object(fileObject)
                window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget, "categoryEntity").findChild(QWidget, f"inputContainer{j}").findChild(QWidget, "inputName").setText(fileObject["final"])
            recolor_category(_index, "GRAY")
                # print(fileObject['final'], window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget, "categoryEntity").findChild(QWidget, f"inputContainer{j}").findChild(QWidget, "inputName").text(), window.filesObjects[_index][j]["final"])
                # window.categoryInputs[_index][j].setText(fileObject["final"])
                # set_in_2D_list("filesObjects", _index, j, fileObject)
        
    def refresh_datas() :
        """Refresh all the datas
        """        
        [ refresh_data(i) for i in range(len(window.filesNames)) ]
    
    def get_folder() -> str :
        """Open a file dialog to get a folder path

        Returns:
            str: The path of the folder
        """
        # print("It was", pathFolder)
        # QFileDialog.getExistingDirectory()
        pathFolder = QFileDialog.getExistingDirectory(None, gc.FILE_DIALOG_CAPTION, 
                                                      "C:/Users/user/Downloads/Telegram Desktop")
                                                    #   os.path.join( pathToMyDocuments ))
        window.m_ui.folderNameEdit.setText(pathFolder)
        print("It is", window.m_ui.folderNameEdit.text())
        if pathFolder != "" :
            compileFiles(window.m_ui.folderNameEdit.text()) 
        return pathFolder        
    
    def goToPage(page : str) :
        """Go to the specified page

        Args:
            page (str): The destination page
        """        
        actualPage = page
        window.setWindowTitle( QCoreApplication.translate("CallmeBack", gc.PAGES_TITLES[page], None) )
        window.stackedWidget.setCurrentIndex(gc.PAGES_INDEX[page])
        activePage(page)
    
    # Create pages and load ui files in it
    window.__setattr__("renamer", gf.load_py("renamer"))
    window.m_ui.parcourirButton.clicked.connect(lambda : get_folder())
    window.m_ui.actionParcourir.triggered.connect(lambda : get_folder())
    window.m_ui.actionParcourir.setShortcut('Ctrl+B')
    window.m_ui.actionUndo.triggered.connect(lambda : undo())
    window.m_ui.actionUndo.setShortcut('Ctrl+Z')
    window.m_ui.actionRedo.triggered.connect(lambda : redo())
    window.m_ui.actionRedo.setShortcut('Ctrl+Shift+Z')
    window.m_ui.actionTout_Rafra_chir.triggered.connect(lambda : refresh_datas())
    window.m_ui.actionTout_Rafra_chir.setShortcut('Ctrl+R')
    window.m_ui.actionQuitter.triggered.connect(lambda : form.quit())
    window.m_ui.actionQuitter.setShortcut('Alt+F4')
    window.__setattr__("loader", QMovie(":/loadSpinner/images/rollingSpinner.gif"))
    window.renamer.m_ui.loader.setMovie(window.loader) 
    window.loader.start()
    # window.m_ui.statusbar.addWidget(window.renamer.m_ui.loadSpinner)
    # gf.set_timeout(lambda : window.m_ui.statusbar.removeWidget(window.renamer.m_ui.loadSpinner), 3)
    
    print("It is", window.m_ui.folderNameEdit.text())
    
    # gf.clear_layout(window.m_ui.scrollLayout)
    # for i in range(1,5):
    #         window.__setattr__(f"object{i}", gf.load_py("renamer"))
    #         window.m_ui.scrollLayout.addWidget(window.__getattribute__(f'object{i}').m_ui.categoryGroup)
    
    # window.__setattr__("template", gf.load_py("template"))
    # window.stackedWidget.addWidget(window.template)
    # window.template.m_ui.template_1.clicked.connect(lambda : goToPage("template"))
    # window.template.m_ui.template_2.clicked.connect(lambda : goToPage("template_2"))
    # window.__setattr__("template_2", gf.load_py("template_2"))
    # window.stackedWidget.addWidget(window.template_2)
    # window.template_2.m_ui.template_1.clicked.connect(lambda : goToPage("template"))
    # window.template_2.m_ui.template_2.clicked.connect(lambda : goToPage("template_2"))
    
    window.show()
    form.exec_()