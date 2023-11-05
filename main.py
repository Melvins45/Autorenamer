import typing
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QFile, QTextStream, QIODevice, Signal, QThread, SignalInstance, QRegExp)
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
import copy

class CategoriesStatus(Enum) :
    NOT_TREATED = 0
    TREATED = 1

class CategoriesColors(Enum) :
    GREEN = ["rgb(28,255,81)", "rgb(126,255,152)"]
    GRAY = ["rgb(217,217,217)", "rgb(241,241,241)"]

class Worker(QObject) :
    finished = Signal()
    runnerSignal = Signal()
    def __init__(self, parent = None,runner = None) -> None:
        super().__init__(parent=parent)
        self.runnerFunction = runner
        
    def run(self) :
        if self.runnerFunction != None :
            self.runnerFunction()
        self.runnerSignal.emit()
        # print("Yes")
        self.finished.emit()

class SimpleWorker(QObject) :
    finished = Signal()
    runnerSignal = Signal()
    def __init__(self, runner) -> None:
        super().__init__(None)
        self.runner = runner
        
    def run(self) :
        if self.runner != None :
            self.runner()
        self.runnerSignal.emit()
        # print("Yes")
        self.finished.emit()

class TimerWorker(QObject) :
    finished = Signal()
    # finisherSignal = Signal()
    runnerSignal = Signal()
    def __init__(self, runner, secs = 2, secsAfterRun = 0) -> None:
        super().__init__(None)
        self.runner = runner
        self.secs = secs
        self.secsAfterRun = secsAfterRun
    
    def run(self) :
        time.sleep(self.secs)
        self.runnerSignal.emit()
        if self.runner != None :
            self.runner()
        time.sleep(self.secsAfterRun)
        self.finished.emit()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

actualPage = list(gc.PAGES_TITLES.keys())[0]

oShell = win32com.client.Dispatch("Wscript.Shell")
pathToMyDocuments = oShell.SpecialFolders("MyDocuments")

def main():
# if __name__ == "__main__":
    # pathFolder = ""
    
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
    window.__setattr__("undoActions", [])
    window.__setattr__("previousPathFolders", [])
    window.__setattr__("filesPreviousNames", [])
    window.__setattr__("filesPreviousObjects", [])
    window.__setattr__("filesPreviousOriginalsNames", [])
    window.__setattr__("filesPreviousOriginalsObjects", [])
    window.__setattr__("filesOriginalsNames", [])
    window.__setattr__("filesOriginalsObjects", [])
    window.__setattr__("categoriesNamesInputs", [])
    window.__setattr__("categoryInputs", [])
    window.__setattr__("canCreateNewFolder", [])
    window.__setattr__("canDivideBySeason", [])
    # window.__setattr__("originalsCanCreateNewFolder", [])
    window.__setattr__("previousCanCreateNewFolder", [])
    # window.__setattr__("categoryInputsLabels", [])
    window.__setattr__("categoriesStatus", [])
    window.__setattr__("undoIndex", -1)
    window.__setattr__("indexToaster", 0)
    window.__setattr__("hadShownAll", False)
    window.__setattr__("indexStartRename", -1)
    
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
        files_names = [ i for i in files_names if [ j in i for j in files_names ].count(True) < 2 ] 
        files_sorted = [ [ j for j in filesyly if i in gf.capitalise_all(j["name"]) ] for i in files_names ]
        files_sorted = [ sorted(i, key=itemgetter('episode')) for i in files_sorted ]
        
        # Put the resulted objects in a state
        if len(window.filesNames) != 0 :
            window.undoActions.clear()
            window.userActions.append(Action.Action(Action.TypeActions["BROWSE"], -1, None, {
                "pathFolder" : window.pathFolder,
                "filesNames" : window.filesNames.copy(),
                "filesObjects" : copy.deepcopy(window.filesObjects),
                "filesOriginalsNames" : window.filesOriginalsNames.copy(),
                "filesOriginalsObjects" : copy.deepcopy(window.filesOriginalsObjects),
                "canCreateNewFolder" : window.canCreateNewFolder.copy(),
                "canDivideBySeason" : window.canDivideBySeason.copy(),
                "categoriesNamesInputs" : window.categoriesNamesInputs.copy(),
                "categoriesStatus" : window.categoriesStatus.copy(),
            } ))
        window.pathFolder = _pathFolder
        window.pathFolder = window.pathFolder.replace('/','\\')
        window.filesNames = files_names.copy()
        window.filesObjects = copy.deepcopy(files_sorted)
        window.filesOriginalsNames = window.filesNames.copy()
        window.filesOriginalsObjects = copy.deepcopy(window.filesObjects)
        window.canCreateNewFolder = [ False for i in files_names ]
        window.canDivideBySeason = [ False for i in files_names ]
        window.categoriesNamesInputs = [ QLineEdit(i) for i in files_names ]
        window.categoriesStatus = [ CategoriesStatus.NOT_TREATED.value for i in files_names ]
        # window.originalsCanCreateNewFolder = [ False for i in files_names ]
        
        if len(window.filesObjects) != 0 :
            show_categories(files_names, files_sorted)
        else :
            gf.remove_from_status_bar(window.m_ui.statusbar, window.m_ui.statusbar.findChild(QWidget, "loadSpinner"))   
        # print(gf.get_name_from_object(files_sorted[0][0]))
        # print( gf.get_episode_object(gf.get_name_from_object(files_sorted[0][0])) )
        return files_sorted
        
    def thread_category(_index : int, _max_index : int) :
        
        # Init worker and thread
        window.__setattr__(f"compilerThread{_index}", QThread())
        window.__setattr__(f"compilerWorker{_index}", TimerWorker( lambda i=_index : None, 0 ))
        
        # Connect worker to thread and other relative signals
        window.__getattribute__(f"compilerWorker{_index}").moveToThread(window.__getattribute__(f"compilerThread{_index}")) 
        window.__getattribute__(f"compilerWorker{_index}").runnerSignal.connect(lambda i=_index : show_category(i) )
        window.__getattribute__(f"compilerThread{_index}").started.connect(window.__getattribute__(f"compilerWorker{_index}").run)
        window.__getattribute__(f"compilerWorker{_index}").finished.connect(window.__getattribute__(f"compilerThread{_index}").quit)
        window.__getattribute__(f"compilerWorker{_index}").finished.connect(lambda : thread_category(_index+1, _max_index) if _index != _max_index else (window.compilerAllThread.start(), connect_all_widgets(), window.__setattr__("hadShownAll", True)))
        window.__getattribute__(f"compilerWorker{_index}").finished.connect(window.__getattribute__(f"compilerWorker{_index}").deleteLater)
        window.__getattribute__(f"compilerThread{_index}").finished.connect(window.__getattribute__(f"compilerThread{_index}").deleteLater)
        
        # Start the thread
        window.__getattribute__(f"compilerThread{_index}").start()

    def toast_ok(_index : int, _message : str) :
        
        # Init worker, thread and label
        _index = window.indexToaster
        window.indexToaster += 1
        window.__setattr__(f"okThread{_index}", QThread())
        window.__setattr__(f"okWorker{_index}", TimerWorker( lambda i=_index : None, 0, 2 ))
        window.__setattr__(f"okLabel{_index}", gf.load_py("renamer"))
        
        window.__getattribute__(f"okLabel{_index}").m_ui.completedMessage.setObjectName(f"okMessage{_index}")
        window.__getattribute__(f"okLabel{_index}").m_ui.completedLabel.setText(_message)
        
        # Connect worker to thread and other relative signals
        window.__getattribute__(f"okWorker{_index}").moveToThread(window.__getattribute__(f"okThread{_index}")) 
        window.__getattribute__(f"okWorker{_index}").runnerSignal.connect(lambda i=_index : window.m_ui.statusbar.addWidget(window.__getattribute__(f"okLabel{_index}").m_ui.completedMessage) )
        window.__getattribute__(f"okThread{_index}").started.connect(window.__getattribute__(f"okWorker{_index}").run)
        window.__getattribute__(f"okWorker{_index}").finished.connect(lambda : gf.remove_from_status_bar(window.m_ui.statusbar, window.m_ui.statusbar.findChild(QWidget, f"okMessage{_index}")))
        window.__getattribute__(f"okWorker{_index}").finished.connect(window.__getattribute__(f"okThread{_index}").quit)
        window.__getattribute__(f"okWorker{_index}").finished.connect(window.__getattribute__(f"okWorker{_index}").deleteLater)
        window.__getattribute__(f"okThread{_index}").finished.connect(window.__getattribute__(f"okThread{_index}").deleteLater)
        
        # Start the thread
        window.__getattribute__(f"okThread{_index}").start()
        
    def toast_error(_index : int, _message : str) :
        
        # Init worker, thread and label
        _index = window.indexToaster
        window.indexToaster += 1
        window.__setattr__(f"errorThread{_index}", QThread())
        window.__setattr__(f"errorWorker{_index}", TimerWorker( lambda i=_index : None, 0, 2 ))
        window.__setattr__(f"errorLabel{_index}", gf.load_py("renamer"))
        
        window.__getattribute__(f"errorLabel{_index}").m_ui.errorMessage.setObjectName(f"errorMessage{_index}")
        window.__getattribute__(f"errorLabel{_index}").m_ui.errorLabel.setText(_message)
        
        # Connect worker to thread and other relative signals
        window.__getattribute__(f"errorWorker{_index}").moveToThread(window.__getattribute__(f"errorThread{_index}")) 
        window.__getattribute__(f"errorWorker{_index}").runnerSignal.connect(lambda i=_index : window.m_ui.statusbar.addWidget(window.__getattribute__(f"errorLabel{_index}").m_ui.errorMessage) )
        window.__getattribute__(f"errorThread{_index}").started.connect(window.__getattribute__(f"errorWorker{_index}").run)
        window.__getattribute__(f"errorWorker{_index}").finished.connect(lambda : gf.remove_from_status_bar(window.m_ui.statusbar, window.m_ui.statusbar.findChild(QWidget, f"errorMessage{_index}")))
        window.__getattribute__(f"errorWorker{_index}").finished.connect(window.__getattribute__(f"errorThread{_index}").quit)
        window.__getattribute__(f"errorWorker{_index}").finished.connect(window.__getattribute__(f"errorWorker{_index}").deleteLater)
        window.__getattribute__(f"errorThread{_index}").finished.connect(window.__getattribute__(f"errorThread{_index}").deleteLater)
        
        # Start the thread
        window.__getattribute__(f"errorThread{_index}").start()
        
    def show_categories(_files_names: list[str], _files_sorted: list[list[dict]]) :
        """Show in the GUI the sorted files

        Args:
            _files_names (list[str]): The names of categories
            _files_sorted (list[list[dict]]): The sorted files to show
        """
        # return
        gf.clear_layout(window.m_ui.scrollLayout)
        
        # Init worker and thread
        window.__setattr__("compilerAllThread", QThread())
        window.__setattr__("compilerAllWorker", SimpleWorker( lambda : window.compilingAll.emit("fr") ))
        
        # Connect worker to thread and other relative signals
        window.compilerAllWorker.moveToThread(window.compilerAllThread) 
        gf.reconnect(window.compilingAll, lambda : gf.remove_from_status_bar(window.m_ui.statusbar, window.m_ui.statusbar.findChild(QWidget, "loadSpinner")))
        window.compilerAllThread.started.connect(window.compilerAllWorker.run)
        window.compilerAllWorker.finished.connect(window.compilerAllThread.quit)
        window.compilerAllWorker.finished.connect(window.compilerAllWorker.deleteLater)
        window.compilerAllThread.finished.connect(window.compilerAllThread.deleteLater)
        
        # Dealing with threads
        thread_category(0, len(_files_names)-1)
        # [ show_category(i) for i in range(len(window.filesNames)) ]
        # connect_all_widgets()
        
    def show_category(_index : int) :
        """Show the category 

        Args:
            _index (int): The index of the category to show
        """
        # print(" Index is ", _index," and len is ", len(window.filesObjects)-1)
        window.__setattr__(f"category{_index}", gf.load_py("renamer"))
        window.__setattr__(f"categoryLayout{_index}", QVBoxLayout())
        window.__getattribute__(f"categoryLayout{_index}").setObjectName(f"categoryLayout{_index}")
        for j in range(len(window.filesObjects[_index])) :
            window.__setattr__(f"category{_index}-{j}", gf.load_py("renamer"))
            if j == 0 :
                window.__getattribute__(f"category{_index}-{j}").m_ui.category.setText(window.filesNames[_index])
                window.__getattribute__(f"categoryLayout{_index}").addWidget(window.__getattribute__(f"category{_index}-{j}").m_ui.categoryContainer) 
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
        # window.__getattribute__(f"category{_index}-{j}").m_ui.category.setText(window.filesNames[_index])
        # window.__getattribute__(f"categoryLayout{_index}").addWidget(window.__getattribute__(f"category{_index}-{j}").m_ui.oddContainer) 
        gf.clear_layout(window.__getattribute__(f'category{_index}').m_ui.categoryLayout)
        window.__getattribute__(f'category{_index}').m_ui.categoryLayout.addLayout(window.__getattribute__(f'categoryLayout{_index}'))
        # window.__getattribute__(f"category{_index}").m_ui.category.setText(window.filesNames[_index])
        window.m_ui.scrollLayout.addWidget(window.__getattribute__(f'category{_index}').m_ui.categoryGroup)
        
    def insert_category(_index : int) :
        """Insert the category to the index 

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
        window.m_ui.scrollLayout.insertWidget(_index, window.__getattribute__(f'category{_index}').m_ui.categoryGroup)
        
    def refresh_category(_index : int, _last_datas : list[dict] = None) :
        """Refresh a category

        Args:
            _index (int): The index of the category to show
            _last_datas (list[dict]): The previous datas of the files objects
        """
        # window.__setattr__(f"category{_index}", gf.load_py("renamer"))
        # gf.c
        # print(window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").children())
        
        # Clear the layout of the category
        gf.clear_layout(window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QVBoxLayout,"categoryLayout"))
        
        # Delete the category container
        window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QWidget, "categoryContainer").deleteLater()
        window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QWidget, "categoryContainer").setParent(None)
        
        # Delete all the previous input containers
        [ window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QWidget, f"inputContainer{j}").deleteLater() for j in range(len( window.userActions[-1].datas["filesObjects"][_index] if _last_datas == None else _last_datas )) ]
        [ window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QWidget, f"inputContainer{j}").setParent(None) for j in range(len( window.userActions[-1].datas["filesObjects"][_index] if _last_datas == None else _last_datas )) ]
        # return
        window.__setattr__(f"categoryLayout{_index}", QVBoxLayout())
        window.__getattribute__(f"categoryLayout{_index}").setObjectName(f"categoryLayout{_index}")
        for j in range(len(window.filesObjects[_index])) :
            window.__setattr__(f"category{_index}-{j}", gf.load_py("renamer"))
            if j == 0 :
                window.__getattribute__(f"category{_index}-{j}").m_ui.category.setText(window.filesNames[_index])
                window.__getattribute__(f"categoryLayout{_index}").addWidget(window.__getattribute__(f"category{_index}-{j}").m_ui.categoryContainer)
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
        
    def set_in_2D_dict(_list: str, _first_index : int, _second_index : int, _key : any, _value : any) :
        """Set the value at the index in a specific 2D list of dictionaries of window

        Args:
            _list (str): The name of the list in window
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
        # window.undoIndex = -1
        # window.userActions.append(Action.Action(Action.TypeActions["CHECK_CAN_CREATE_NEW_FOLDER"], _index, _bool, window.canCreateNewFolder.copy()))
        # window.previousDatas["canCreateNewFolder"].append(Action.Action(Action.TypeActions["CHECK_CAN_CREATE_NEW_FOLDER"], _index, _bool, window.canCreateNewFolder))
        # window.previousCanCreateNewFolder.append(window.canCreateNewFolder)
        
        # Updating new datas
        window.canCreateNewFolder[_index] = _bool
        
    def should_divide_by_seasons(_bool: bool, _index: int) :
        
        # Updating new datas
        window.canDivideBySeason[_index] = _bool
        
    def divide_by_seasons(_first_index: int, _second_index: int) :
        """Divide the files by seasons 

        Args:
            _first_index (int): The first index of the file's object
            _second_index (int): The second index of the file's object
        """        
        
        season = "S" + f"{window.filesObjects[_first_index][_second_index]['season']:02}"
            
        # Test if the season's folder is already created
        if not os.path.exists(os.path.join(window.pathFolder, season)) :
            os.makedirs(os.path.join(window.pathFolder, season))
        
        # Rename the original file to the compiled name
        os.rename( os.path.join(window.pathFolder, window.filesOriginalsObjects[_first_index][_second_index]["original"]), os.path.join(window.pathFolder, season, window.filesObjects[_first_index][_second_index]["final"]) )
        
    def create_and_divide_by_seasons(_first_index: int, _second_index: int) :
        """Create a new folder and divide it by season

        Args:
            _first_index (int): The first index of the file object
            _second_index (int): The second index of the file object
        """
        season = "S" + f"{window.filesObjects[_first_index][_second_index]['season']:02}"
        # Test if the englobing folder is already created    
        if not os.path.exists(os.path.join(window.pathFolder, gf.escape_behind_with_pattern(r'\s*$', window.filesNames[_first_index])[0])) :
            os.makedirs(os.path.join(window.pathFolder, gf.escape_behind_with_pattern(r'\s*$', window.filesNames[_first_index])[0]))
            
        # Test if the season's folder is already created
        if not os.path.exists(os.path.join(window.pathFolder, gf.escape_behind_with_pattern(r'\s*$', window.filesNames[_first_index])[0], season)) :
            os.makedirs(os.path.join(window.pathFolder, gf.escape_behind_with_pattern(r'\s*$', window.filesNames[_first_index])[0], season))
        
        # Rename the original file to the compiled name
        os.rename( os.path.join(window.pathFolder, window.filesOriginalsObjects[_first_index][_second_index]["original"]), os.path.join(window.pathFolder, gf.escape_behind_with_pattern(r'\s*$', window.filesNames[_first_index])[0], season, window.filesObjects[_first_index][_second_index]["final"]) )
        
    def create_new_folder(_first_index : int, _second_index : int) :
        """Create a new folder and paste a file in

        Args:
            _first_index (int): The first index of the file object
            _second_index (int): The second index of the file object
        """ 
         
        if not os.path.exists(os.path.join(window.pathFolder, gf.escape_behind_with_pattern(r'\s*$', window.filesNames[_first_index])[0])) :
            os.makedirs(os.path.join(window.pathFolder, gf.escape_behind_with_pattern(r'\s*$', window.filesNames[_first_index])[0]))
        os.rename( os.path.join(window.pathFolder, window.filesOriginalsObjects[_first_index][_second_index]["original"]), os.path.join(window.pathFolder, gf.escape_behind_with_pattern(r'\s*$', window.filesNames[_first_index])[0], window.filesObjects[_first_index][_second_index]["final"]) )
        
    def recolor_category(_index : int, _color : str = "GREEN") :
        
        # print("Who talks : ", _index, " and children are ", window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").children())
        # print("Who talks : ", _index, " and children are ", window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QLayout,"categoryLayout").itemAt(0).widget().objectName())
        
        window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").setStyleSheet( window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").styleSheet() + f"background-color : {CategoriesColors[_color.upper()].value[0]};" )
        window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"category").setStyleSheet( window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"category").styleSheet() + f"background-color : {CategoriesColors[_color.upper()].value[0]};" )
        window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"close").setStyleSheet( window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"close").styleSheet() + f"background-color : {CategoriesColors[_color.upper()].value[0]};" )
        
        [ window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget, "categoryEntity").findChild(QWidget, f"inputContainer{j}").setStyleSheet( window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget, "categoryEntity").findChild(QWidget, f"inputContainer{j}").styleSheet() + (f"background-color : {CategoriesColors[_color.upper()].value[1]};" if j%2 == 0 else "") ) for j in range(len(window.filesObjects[_index])) ]
        
        window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"refresh").setStyleSheet( window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"refresh").styleSheet() + f"background-color : {CategoriesColors[_color.upper()].value[1]};" )
        window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"renameAll").setStyleSheet( window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"renameAll").styleSheet() + f"background-color : {CategoriesColors[_color.upper()].value[1]};" )
        window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"fuseWith").setStyleSheet( window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"fuseWith").styleSheet() + f"background-color : {CategoriesColors[_color.upper()].value[1]};" )
        window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"renameInAscendingOrder").setStyleSheet( window.m_ui.scrollLayout.itemAt(_index).widget().findChild(QWidget,"renameInAscendingOrder").styleSheet() + f"background-color : {CategoriesColors[_color.upper()].value[1]};" )
        
    def rename_all_categories() :
        window.indexStartRename = -1
        window.undoActions.clear()
        window.userActions.append(Action.Action(Action.TypeActions["RENAME_ALL_CATEGORIES"], -1, None, { "categoriesStatus" : window.categoriesStatus.copy(),
          "canDivideBySeason" : window.canDivideBySeason.copy(),
          "canCreateNewFolder" : window.canCreateNewFolder.copy() }))
        [ rename_all(i, True) for i in range(len(window.filesNames)) ]
        
    def rename_all(_index : int, _concern_all : bool = False) :
        
        # Testing if the files' category are already renamed
        if window.categoriesStatus[_index] == CategoriesStatus.TREATED.value :
            return
        
        # Saving previous datas and the first index to rename
        if not _concern_all :
            window.undoActions.clear()
            if window.canCreateNewFolder[_index] and window.canDivideBySeason[_index] :
                window.undoIndex = -1
                window.userActions.append(Action.Action(Action.TypeActions["CREATE_AND_DIVIDE_BY_SEASONS"], _index, window.filesNames[_index], { "categoriesStatus" : window.categoriesStatus.copy() }))
            elif window.canDivideBySeason[_index] :
                window.undoIndex = -1
                window.userActions.append(Action.Action(Action.TypeActions["DIVIDE_BY_SEASONS"], _index, window.filesNames[_index], { "categoriesStatus" : window.categoriesStatus.copy() }))
            elif window.canCreateNewFolder[_index] :
                window.undoIndex = -1
                window.userActions.append(Action.Action(Action.TypeActions["CREATE_NEW_FOLDER"], _index, window.filesNames[_index], { "categoriesStatus" : window.categoriesStatus.copy() }))
            else :
                window.undoIndex = -1
                window.userActions.append(Action.Action(Action.TypeActions["RENAME_ALL"], _index, None, { "categoriesStatus" : window.categoriesStatus.copy() }))
        elif window.indexStartRename == -1 :
            window.indexStartRename = _index
        
        # Do the divide by seasons treatment
        
        [ create_and_divide_by_seasons(_index, j) if window.canCreateNewFolder[_index] and window.canDivideBySeason[_index] else
         divide_by_seasons(_index, j) if window.canDivideBySeason[_index] else
         create_new_folder(_index, j) if window.canCreateNewFolder[_index] 
         else os.rename( os.path.join(window.pathFolder, window.filesOriginalsObjects[_index][j]["original"]), os.path.join(window.pathFolder, window.filesObjects[_index][j]["final"]) ) 
         for j in range(len(window.filesObjects[_index])) ]
        window.categoriesStatus[_index] = CategoriesStatus.TREATED.value
        recolor_category(_index)
        if window.indexStartRename == _index and _concern_all :
            toast_ok(_index, f"Toutes catégories renommées !")
        elif not _concern_all :
            toast_ok(_index, f"Renommé avec succès !")
        # toast_ok(_index, f"{window.filesNames[_index]} renommée avec succès !")
        
    def undo_rename_all_categories() :
        # Régler le problème des rename all undo
        window.categoriesStatus = window.userActions[-1].datas["categoriesStatus"]
        season = lambda _index, _second_index : "S" + f"{window.filesObjects[_index][_second_index]['season']:02}"
        
        [ 
         # Test if both canCreateNewFolder and canDivideBySeason 's checkboxes are checked
         (
        [ os.rename( os.path.join(window.pathFolder, gf.escape_behind_with_pattern(r'\s*$', window.filesNames[i])[0], season(i, j), window.filesObjects[i][j]["final"]), os.path.join(window.pathFolder, window.filesOriginalsObjects[i][j]["original"]) ) for j in range(len(window.filesObjects[i])) ]
        if not False in [ os.path.exists(os.path.join(window.pathFolder, gf.escape_behind_with_pattern(r'\s*$', window.filesNames[i])[0], season(i, j))) for j in range(len(window.filesObjects[i])) ] else None
        ) if window.userActions[-1].datas["canCreateNewFolder"][i] and window.userActions[-1].datas["canDivideBySeason"][i] else
         
         # Else test if canDivideBySeason's checkboxe is checked
         (
        [ os.rename( os.path.join(window.pathFolder, season(i,j), window.filesObjects[i][j]["final"]), os.path.join(window.pathFolder, window.filesOriginalsObjects[i][j]["original"]) ) for j in range(len(window.filesObjects[i])) ]
        if not False in [ os.path.exists(os.path.join(window.pathFolder, season(i, j))) for j in range(len(window.filesObjects[i])) ] else None
        ) if window.userActions[-1].datas["canDivideBySeason"][i] else
         
         # Else test if canCreateNewFolder's checkboxe is checked
         (
        [ os.rename( os.path.join(window.pathFolder, gf.escape_behind_with_pattern(r'\s*$', window.filesNames[i])[0], window.filesObjects[i][j]["final"]), os.path.join(window.pathFolder, window.filesOriginalsObjects[i][j]["original"]) ) for j in range(len(window.filesObjects[i])) ]
        if os.path.exists(os.path.join(window.pathFolder, window.filesNames[i])) else None
        ) if window.userActions[-1].datas["canCreateNewFolder"][i] else
         
         # Else do the normal renaming
        [ os.rename( os.path.join(window.pathFolder, window.filesObjects[i][j]["final"]), os.path.join(window.pathFolder, window.filesOriginalsObjects[i][j]["original"]) ) for j in range(len(window.filesObjects[i])) ]  
         
         # Take only indices where the previous categoriesStatus are not treated so that the actual are treated
        for i in range(len(window.filesNames)) if window.categoriesStatus[i] != CategoriesStatus.TREATED.value ]
        
        [ recolor_category(i, "GRAY") for i in range(len(window.filesNames)) if window.categoriesStatus[i] != CategoriesStatus.TREATED.value ]
        
    def undo_rename_all() :
        """Undo the action rename all
        """        
        _index = window.userActions[-1].concernIndex
        [ os.rename( os.path.join(window.pathFolder, window.filesObjects[_index][j]["final"]), os.path.join(window.pathFolder, window.filesOriginalsObjects[_index][j]["original"]) ) for j in range(len(window.filesObjects[_index])) ]
        window.categoriesStatus[_index] = window.userActions[-1].datas["categoriesStatus"][_index]
        recolor_category(_index, "GRAY")
        
    def undo_create_new_folder() :
        """Undo the action create new folder and rename all
        """        
        _index = window.userActions[-1].concernIndex
        if not os.path.exists(os.path.join(window.pathFolder, gf.escape_behind_with_pattern(r'\s*$', window.filesNames[_index])[0])) :
            return
        [ os.rename( os.path.join(window.pathFolder, gf.escape_behind_with_pattern(r'\s*$', window.filesNames[_index])[0], window.filesObjects[_index][j]["final"]), os.path.join(window.pathFolder, window.filesOriginalsObjects[_index][j]["original"]) ) for j in range(len(window.filesObjects[_index])) ]
        window.categoriesStatus[_index] = window.userActions[-1].datas["categoriesStatus"][_index]
        recolor_category(_index, "GRAY")
        
    def undo_create_and_divide_by_seasons() :
        _index = window.userActions[-1].concernIndex
        season = lambda _second_index : "S" + f"{window.filesObjects[_index][_second_index]['season']:02}"
        
        if False in [ os.path.exists(os.path.join(window.pathFolder, gf.escape_behind_with_pattern(r'\s*$', window.filesNames[_index])[0], season(j))) for j in range(len(window.filesObjects[_index])) ] :
            return
        [ os.rename( os.path.join(window.pathFolder, gf.escape_behind_with_pattern(r'\s*$', window.filesNames[_index])[0], season(j), window.filesObjects[_index][j]["final"]), os.path.join(window.pathFolder, window.filesOriginalsObjects[_index][j]["original"]) ) for j in range(len(window.filesObjects[_index])) ]
        window.categoriesStatus[_index] = window.userActions[-1].datas["categoriesStatus"][_index]
        recolor_category(_index, "GRAY")
        
    def undo_divide_by_seasons() :
        """Undo the action divide by seasons
        """        
        _index = window.userActions[-1].concernIndex
        season = lambda _second_index : "S" + f"{window.filesObjects[_index][_second_index]['season']:02}"
        
        if False in [ os.path.exists(os.path.join(window.pathFolder, season(j))) for j in range(len(window.filesObjects[_index])) ] :
            return
        [ os.rename( os.path.join(window.pathFolder, season(j), window.filesObjects[_index][j]["final"]), os.path.join(window.pathFolder, window.filesOriginalsObjects[_index][j]["original"]) ) for j in range(len(window.filesObjects[_index])) ]
        window.categoriesStatus[_index] = window.userActions[-1].datas["categoriesStatus"][_index]
        recolor_category(_index, "GRAY")
        
    def connect_all_widgets():
        """Connect all the widgets of the scrollLayout
        """        
        # Connect the categories' names inputs to our state
        [ gf.reconnect(window.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"category").textChanged, lambda _=0, i=i : window.categoriesNamesInputs[i].setText(_) ) for i in range(len(window.filesNames)) ]
        
        # Connect the editingFinished signal of categories' names inputs to the click of the refresh button of the category
        [ gf.reconnect(window.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"category").editingFinished, lambda _=0, i=i : window.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"refresh").animateClick() ) for i in range(len(window.filesNames)) ]
        
        # Connect the categories' items inputs to our state
        [  [ gf.reconnect(window.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget, "categoryEntity").findChild(QWidget, f"inputContainer{j}").findChild(QWidget, "inputName").textChanged, lambda _=0, i=i, j=j : set_in_2D_dict("filesObjects", i, j, "final", _) ) for j in range(len(window.filesObjects[i])) ] for i in range(len(window.filesNames))  ]
        
        # Connect the returnPressed of each category item input to the focus of the next
        [  [ gf.reconnect(window.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget, "categoryEntity").findChild(QWidget, f"inputContainer{j}").findChild(QWidget, "inputName").returnPressed, lambda _=0, i=i, j=j : window.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget, "categoryEntity").findChild(QWidget, f"inputContainer{j+1}").findChild(QWidget, "inputName").setFocus() if j+1 < len(window.filesObjects[i]) else None ) for j in range(len(window.filesObjects[i])) ] for i in range(len(window.filesNames))  ]
        
        # Connect each category button to his function
        [ gf.reconnect(window.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"refresh").clicked, lambda _=0, i=i : refresh_data(i)) for i in range(len(window.filesNames)) ]
        [ gf.reconnect(window.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"renameAll").clicked, lambda _=0, i=i : rename_all(i)) for i in range(len(window.filesNames)) ]
        [ gf.reconnect(window.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"fuseWith").clicked, lambda _=0, i=i : fuse_with(i)) for i in range(len(window.filesNames)) ]
        [ gf.reconnect(window.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"createNewFolder").toggled, lambda _, i=i : should_create_new_folder(_,i)) for i in range(len(window.filesNames)) ]
        [ gf.reconnect(window.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"divideBySeasons").toggled, lambda _, i=i : should_divide_by_seasons(_,i)) for i in range(len(window.filesNames)) ]
        [ gf.reconnect(window.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"renameInAscendingOrder").clicked, lambda _=0, i=i : rename_in_ascending_order(i)) for i in range(len(window.filesNames)) ]
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
        window.undoActions.clear()
        window.undoIndex = -1
        window.userActions.append(Action.Action(Action.TypeActions["FUSE_WITH"], _who, _where, {
            "filesNames" : window.filesNames[_who],
            "filesObjects" : copy.deepcopy(window.filesObjects),
            "filesOriginalsNames" : window.filesOriginalsNames[_who],
            "filesOriginalsObjects" : copy.deepcopy(window.filesOriginalsObjects),
            "canCreateNewFolder" : copy.copy(window.canCreateNewFolder[_who]),
            "categoriesStatus" : copy.copy(window.categoriesStatus[_who]),
            "categoriesNamesInputs" : window.categoriesNamesInputs[_who]
        }))
        
        # Copying the datas of the _who category in the _where category
        window.filesObjects[_where].extend(window.filesObjects[_who])        
        window.filesObjects[_where] = sorted(window.filesObjects[_where], key=itemgetter('episode'))
        window.filesOriginalsObjects[_where].extend(window.filesOriginalsObjects[_who])        
        window.filesOriginalsObjects[_where] = sorted(window.filesOriginalsObjects[_where], key=itemgetter('episode'))
        res = []
        [ res.append(x) for x in window.filesOriginalsObjects[_where] if x not in res ]
        window.filesOriginalsObjects[_where] = res.copy()

        # Finish with the remaining tasks
        refresh_category(_where)
        close_group(_who, True)
        window.fuser.close()
                
    def fuse_with(_index : int) :
        """Open a popup widget to pick a category to fuse the given one in

        Args:
            _index (int): The index of the category to fuse in another
        """        
        if len(window.filesNames) == 1 :
            toast_error(_index, "Nombre de catégories insuffisant")
            return
        window.__setattr__('fuser', gf.load_py('fuser_dialog'))
        fontDatabase = QFontDatabase()
        fontDatabase.addApplicationFont(resource_path("fonts\\inder.ttf"))
        window.fuser.setFont(QFont(fontDatabase.applicationFontFamilies(0)[0], 10))
        # window.fuser.setWindowFlags(Qt.WindowStaysOnTopHint)
        # window.fuser.setAttribute(Qt.WA_DeleteOnClose)
        radios = []
        for i in range(len(window.filesObjects)) :
            if i != _index :
                window.__setattr__(f"fuser{i}", gf.load_py('renamer'))
                window.__getattribute__(f"fuser{i}").m_ui.categoryRadio.setText(gf.autoWrap(window.filesNames[i], 80))
                window.__getattribute__(f"fuser{i}").m_ui.categoryRadio.toggled.connect(lambda _, i=i : radios.append( i ) if _ == True else None) # set_in_dict(radios, window.filesNames[i], _)) # print(window.filesNames[i], _))
                window.fuser.m_ui.scrollLayout.addWidget(window.__getattribute__(f"fuser{i}").m_ui.categoryRadio)
        window.fuser.m_ui.ok.clicked.connect(lambda _='t' : fuse_categories(radios[-1] if len(radios) != 0 else None, _index))
        window.fuser.exec_()
        # window.fuser.show()
        
    def close_group(_index : int, isFusing : bool = False) :
        """Close and delete a category

        Args:
            _index (int): The index of the category
            isFusing (bool): A bool to know if the user are fusing categories. Defaults to False.
        """        
        # Saving the previous datas
        if not isFusing :
            window.undoActions.clear()
            window.undoIndex = -1
            window.userActions.append(Action.Action(Action.TypeActions["CLOSE_GROUP"], _index, None, {
                "filesNames" : copy.copy(window.filesNames[_index]),
                "filesObjects" : copy.deepcopy(window.filesObjects[_index]),
                "filesOriginalsNames" : copy.copy(window.filesOriginalsNames[_index]),
                "filesOriginalsObjects" : copy.deepcopy(window.filesOriginalsObjects[_index]),
                "canCreateNewFolder" : copy.copy(window.canCreateNewFolder[_index]),
                "categoriesStatus" : copy.copy(window.categoriesStatus[_index]),
                "categoriesNamesInputs" : window.categoriesNamesInputs[_index]
            }))
        window.filesPreviousNames.append(window.filesNames.copy())
        window.filesPreviousObjects.append(window.filesObjects.copy())
        window.filesPreviousOriginalsNames.append(window.filesOriginalsNames.copy())
        window.filesPreviousOriginalsObjects.append(window.filesOriginalsObjects.copy())
        window.previousCanCreateNewFolder.append(window.canCreateNewFolder.copy())
        # window.previousOriginalsCanCreateNewFolder.append(window.previousOriginalsCanCreateNewFolder.copy())
        # print("before delete ", window.filesNames[_index])
        
        # Delete the index of category to close
        # print(_index, len(window.filesNames)-1)
        del window.filesNames[_index]
        del window.filesObjects[_index]
        del window.filesOriginalsNames[_index]
        del window.filesOriginalsObjects[_index]
        del window.categoriesNamesInputs[_index]
        # del window.categoryInputs[_index]
        del window.canCreateNewFolder[_index]
        del window.categoriesStatus[_index]
        # del window.originalsCanCreateNewFolder[_index]
        # print("After ", _index, len(window.filesNames)-1)
        # print("after delete ", window.filesNames[_index])
        
        # Remove it from layout
        gf.remove_from_layout(window.m_ui.scrollLayout, _index)
        if len(window.filesObjects) == 0 :
            # print("Yes")
            window.__setattr__("emptySearch", gf.load_py("renamer"))
            window.emptySearch.m_ui.noFileFound.setText("Toutes les catégories sont fermées. Annulez votre dernière action ou parcourez un autre dossier pour en afficher")
            window.m_ui.scrollLayout.addWidget(window.emptySearch.m_ui.emptySearch)
        
        # Reconnect all widgets
        connect_all_widgets()
        
    def rename_in_ascending_order(_index: int) :
        """Rename a category in the ascending order

        Args:
            _index (int): The index of the category
        """
        window.undoActions.clear()
        window.undoIndex = -1
        window.userActions.append(Action.Action(Action.TypeActions["RENAME_IN_ASCENDING_ORDER"], _index, None, {
            "filesObjects" : copy.deepcopy(window.filesObjects[_index]),
        }))
        [ set_in_2D_dict("filesObjects", _index, j, "episode", j+1) for j in range(len(window.filesObjects[_index])) ]
        [ set_in_2D_dict("filesObjects", _index, j, "final", gf.get_name_from_object(window.filesObjects[_index][j])) for j in range(len(window.filesObjects[_index])) ]
        refresh_category(_index, window.userActions[-1].datas["filesObjects"])
        connect_all_widgets()
        
    def undo() :
        if len(window.userActions) == 0 :
            return
        match window.userActions[-1].type.name :
            case "RENAME_ALL" :
                undo_rename_all()
            case "REFRESH" :
                window.filesNames[window.userActions[-1].concernIndex] = window.userActions[-1].datas["filesNames"]
                window.filesObjects[window.userActions[-1].concernIndex] = window.userActions[-1].datas["filesObjects"]
                # [window.userActions[-1].concernIndex]
                [ window.m_ui.scrollLayout.itemAt(window.userActions[-1].concernIndex).widget().findChild(QWidget, "categoryEntity").findChild(QWidget, f"inputContainer{j}").findChild(QWidget, "inputName").setText(window.userActions[-1].datas["filesObjects"][j]["final"]) for j in range(len(window.userActions[-1].datas["filesObjects"])) ]
                # set_in_2D_list("filesObjects", window.userActions[-1].concernIndex, j, fileObject)
            case "CLOSE_GROUP" :
                if len(window.filesNames) == 0 :
                    gf.clear_layout(window.m_ui.scrollLayout)
                window.filesNames.insert(window.userActions[-1].concernIndex, window.userActions[-1].datas["filesNames"])
                window.filesObjects.insert(window.userActions[-1].concernIndex, window.userActions[-1].datas["filesObjects"])
                window.filesOriginalsNames.insert(window.userActions[-1].concernIndex, window.userActions[-1].datas["filesOriginalsNames"])
                window.filesOriginalsObjects.insert(window.userActions[-1].concernIndex, window.userActions[-1].datas["filesOriginalsObjects"])
                window.categoriesNamesInputs.insert(window.userActions[-1].concernIndex, window.userActions[-1].datas["categoriesNamesInputs"])
                window.canCreateNewFolder.insert(window.userActions[-1].concernIndex, window.userActions[-1].datas["canCreateNewFolder"])
                window.categoriesStatus.insert(window.userActions[-1].concernIndex, window.userActions[-1].datas["categoriesStatus"])
                insert_category(window.userActions[-1].concernIndex)
                connect_all_widgets()
            case "FUSE_WITH" :
                # print("Undo Fusing")
                window.filesNames.insert(window.userActions[-1].concernIndex, window.userActions[-1].datas["filesNames"])
                window.filesObjects = window.userActions[-1].datas["filesObjects"]
                window.filesOriginalsNames.insert(window.userActions[-1].concernIndex, window.userActions[-1].datas["filesOriginalsNames"])
                window.filesOriginalsObjects = window.userActions[-1].datas["filesOriginalsObjects"]
                window.categoriesNamesInputs.insert(window.userActions[-1].concernIndex, window.userActions[-1].datas["categoriesNamesInputs"])
                window.canCreateNewFolder.insert(window.userActions[-1].concernIndex, window.userActions[-1].datas["canCreateNewFolder"])
                window.categoriesStatus.insert(window.userActions[-1].concernIndex, window.userActions[-1].datas["categoriesStatus"])
                insert_category(window.userActions[-1].concernIndex)
                refresh_category(window.userActions[-1].concernValue)
                connect_all_widgets()
            case "CREATE_NEW_FOLDER" :
                undo_create_new_folder()
            case "BROWSE" :
                window.pathFolder = window.userActions[-1].datas["pathFolder"]
                window.filesNames = window.userActions[-1].datas["filesNames"]
                window.filesObjects = window.userActions[-1].datas["filesObjects"]
                window.filesOriginalsNames = window.userActions[-1].datas["filesOriginalsNames"]
                window.filesOriginalsObjects = window.userActions[-1].datas["filesOriginalsObjects"]
                window.categoriesNamesInputs = window.userActions[-1].datas["categoriesNamesInputs"]
                window.canCreateNewFolder = window.userActions[-1].datas["canCreateNewFolder"]
                window.categoriesStatus = window.userActions[-1].datas["categoriesStatus"]
                show_categories(window.filesNames, window.filesObjects)
            case "RENAME_ALL_CATEGORIES" :
                undo_rename_all_categories()
            case "RENAME_IN_ASCENDING_ORDER" :
                window.filesObjects[window.userActions[-1].concernIndex] = window.userActions[-1].datas["filesObjects"]
                refresh_category(window.userActions[-1].concernIndex)
                # window.m_ui.scrollLayout.itemAt(window.userActions[-1].concernIndex).widget().findChild(QWidget,"renameInAscendingOrder").animateClick()
                # QCheckBox.isChecked
                connect_all_widgets()
            case "DIVIDE_BY_SEASONS" :
                undo_divide_by_seasons()
            case "CREATE_AND_DIVIDE_BY_SEASONS" :
                undo_create_and_divide_by_seasons()
            
        window.undoActions.append(window.userActions[-1])
        del window.userActions[-1]
        
    def redo() :
        previousUndoActions = window.undoActions.copy()
        if len(window.undoActions) == 0 :
            return
        match window.undoActions[-1].type.name :
            case "RENAME_ALL" :
                rename_all(window.undoActions[-1].concernIndex)
            case "REFRESH" :
                refresh_data(window.undoActions[-1].concernIndex)
            case "CLOSE_GROUP" :
                close_group(window.undoActions[-1].concernIndex)
            case "FUSE_WITH" :
                fuse_categories(window.undoActions[-1].concernValue, window.undoActions[-1].concernIndex)
            case "CREATE_NEW_FOLDER" :
                window.undoIndex = -1
                window.userActions.append(Action.Action(Action.TypeActions["CREATE_NEW_FOLDER"], window.undoActions[-1].concernIndex, window.filesNames[window.undoActions[-1].concernIndex], { "categoriesStatus" : window.categoriesStatus.copy()}))
                [ create_new_folder(window.undoActions[-1].concernIndex, j) for j in range(len(window.filesObjects[window.undoActions[-1].concernIndex])) ]
                window.categoriesStatus[window.undoActions[-1].concernIndex] = CategoriesStatus.TREATED.value
                recolor_category(window.undoActions[-1].concernIndex)
                toast_ok(window.undoActions[-1].concernIndex, f"Renommé avec succès !")
            case "BROWSE" :
                compileFiles(window.m_ui.folderNameEdit.text())
            case "RENAME_ALL_CATEGORIES" :
                rename_all_categories()
            case "RENAME_IN_ASCENDING_ORDER" :
                rename_in_ascending_order(window.userActions[-1].concernIndex)
            case "DIVIDE_BY_SEASONS" :
                window.undoIndex = -1
                window.userActions.append(Action.Action(Action.TypeActions["DIVIDE_BY_SEASONS"], window.undoActions[-1].concernIndex, window.filesNames[window.undoActions[-1].concernIndex], { "categoriesStatus" : window.categoriesStatus.copy()}))
                [ divide_by_seasons(window.undoActions[-1].concernIndex, j) for j in range(len(window.filesObjects[window.undoActions[-1].concernIndex])) ]
                window.categoriesStatus[window.undoActions[-1].concernIndex] = CategoriesStatus.TREATED.value
                recolor_category(window.undoActions[-1].concernIndex)
                toast_ok(window.undoActions[-1].concernIndex, f"Renommé avec succès !")
            case "CREATE_AND_DIVIDE_BY_SEASONS" :
                window.undoIndex = -1
                window.userActions.append(Action.Action(Action.TypeActions["CREATE_AND_DIVIDE_BY_SEASONS"], window.undoActions[-1].concernIndex, window.filesNames[window.undoActions[-1].concernIndex], { "categoriesStatus" : window.categoriesStatus.copy()}))
                [ create_and_divide_by_seasons(window.undoActions[-1].concernIndex, j) for j in range(len(window.filesObjects[window.undoActions[-1].concernIndex])) ]
                window.categoriesStatus[window.undoActions[-1].concernIndex] = CategoriesStatus.TREATED.value
                recolor_category(window.undoActions[-1].concernIndex)
                toast_ok(window.undoActions[-1].concernIndex, f"Renommé avec succès !")
        
        window.undoActions = previousUndoActions.copy()
        del window.undoActions[-1]

    def get_scroll_item(_index : int) :
        print("In scrolle_item ", _index, window.m_ui.scrollLayout.itemAt(_index))
        return window.m_ui.scrollLayout.itemAt(_index)

    def refresh_data(_index : int) :
        """Refresh the datas of the indexed category

        Args:
            _index (int): The index of the category in the whole list
        """        
        if window.filesNames[_index] != window.categoriesNamesInputs[_index].text() :
            # Saving the action
            window.undoActions.clear()
            window.userActions.append(Action.Action(Action.TypeActions["REFRESH"], _index, window.categoriesNamesInputs[_index].text(), {
                "filesNames" : copy.deepcopy(window.filesNames[_index]),
                "filesObjects" : copy.deepcopy(window.filesObjects[_index]),
                "categoriesNamesInputs" : window.categoriesNamesInputs[_index].text()
            }))
            categoryObject = gf.get_episode_object(window.categoriesNamesInputs[_index].text(), True)
            window.filesPreviousNames.append(window.filesNames.copy())
            window.filesPreviousObjects.append(window.filesObjects.copy())
            set_in_list("filesNames", _index, window.categoriesNamesInputs[_index].text())
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
                # set_in_2D_list("filesObjects", _index, j, fileObject)
                window.filesObjects[_index][j] = fileObject
            recolor_category(_index, "GRAY")
        
    def refresh_datas() :
        """Refresh all the datas
        """        
        [ refresh_data(i) for i in range(len(window.filesNames)) ]
    
    def get_folder() -> str :
        """Open a file dialog to get a folder path

        Returns:
            str: The path of the folder
        """
        canCompile = True
        # Check if the actual pathFolder exists or is already used
        if not os.path.exists( rf'{window.m_ui.folderNameEdit.text()}' ) or ( window.previousPathFolders[-1] == window.m_ui.folderNameEdit.text() if len(window.previousPathFolders) != 0 else False ) :
            pathFolder = QFileDialog.getExistingDirectory(None, gc.FILE_DIALOG_CAPTION, 
                                                        "C:/Users/user/Downloads/Telegram Desktop")
                                                        #   os.path.join( pathToMyDocuments ))
            window.m_ui.folderNameEdit.setText(pathFolder)
            window.previousPathFolders.append(pathFolder)
            canCompile = pathFolder != ""
        
        if canCompile :
            # Get the actual pathFolder and actualise the list of previouspathFolders
            pathFolder = rf'{window.m_ui.folderNameEdit.text()}'
            if window.previousPathFolders[-1] != pathFolder if len(window.previousPathFolders) != 0 else False :
                window.previousPathFolders.append(pathFolder)
            print("It is", window.m_ui.folderNameEdit.text())
           
            # Add a loader to the status bar
            window.__setattr__("loader", QMovie(":/loadSpinner/images/rollingSpinner.gif"))
            window.renamer.m_ui.loader.setMovie(window.loader) 
            window.loader.start()
            window.m_ui.statusbar.addWidget(window.renamer.m_ui.loadSpinner)
           
            # Compile with the actual pathFolder
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
    window.__setattr__("scroll_item", get_scroll_item)
    window.m_ui.parcourirButton.clicked.connect(lambda : get_folder())
    window.m_ui.renameAllCategoriesButton.clicked.connect(lambda : rename_all_categories())
    window.m_ui.actionParcourir.triggered.connect(lambda : get_folder())
    window.m_ui.actionParcourir.setShortcut('Ctrl+B')
    window.m_ui.actionUndo.triggered.connect(lambda : undo())
    window.m_ui.actionUndo.setShortcut('Ctrl+Z')
    window.m_ui.actionRedo.triggered.connect(lambda : redo())
    window.m_ui.actionRedo.setShortcut('Ctrl+Shift+Z')
    window.m_ui.actionTout_Renommer.triggered.connect(lambda : rename_all_categories())
    window.m_ui.actionTout_Renommer.setShortcut('Ctrl+F2')
    window.m_ui.actionQuitter.triggered.connect(lambda : form.quit())
    window.m_ui.actionQuitter.setShortcut('Alt+F4')
    
    print("It is", window.m_ui.folderNameEdit.text())
    
    # window.show()
    # form.exec_()
    return window
    
if __name__ == "__main__":
    styleSheetFile = QFile( resource_path("style.qss") )
    styleSheetFile.open(QIODevice.ReadOnly)
    styleSheet = QTextStream(styleSheetFile).readAll()
    form = QApplication(sys.argv)
    fontDatabase = QFontDatabase()
    fontDatabase.addApplicationFont(resource_path("fonts\\inder.ttf"))
    form.setFont(QFont(fontDatabase.applicationFontFamilies(0)[0], 10))
    form.setStyleSheet(styleSheet)
    window = main()
    window.show()
    form.exec_()