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
    window.__setattr__("filesNames", [])
    window.__setattr__("filesObjects", [])
    window.__setattr__("categoriesNamesInputs", [])
    window.__setattr__("categoryInputs", [])
    # window.__setattr__("categoryInputsLabels", [])
    
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
        window.filesNames = files_names.copy()
        window.filesObjects = files_sorted.copy()
        
        showFiles(files_names, files_sorted)   
        # print(gf.get_name_from_object(files_sorted[0][0]))
        # print( gf.get_episode_object(gf.get_name_from_object(files_sorted[0][0])) )
        return files_sorted
        
    def showFiles(_files_names: list[str], _files_sorted: list[list[dict]]) :
        """Show in the GUI the sorted files

        Args:
            _files_names (list[str]): The names of categories
            _files_sorted (list[list[dict]]): The sorted files to show
        """
        # return
        window.categoriesNamesInputs = [ QLabel(i) for i in _files_names ] # _files_names.copy()
        window.categoryInputs = [ [ QLabel(j["final"]) for j in i ] for i in _files_sorted ]
        # window.categoryInputs = [ [ j["final"] for j in i ] for i in _files_sorted ]
        gf.clear_layout(window.m_ui.scrollLayout)
        for i in range(len(_files_names)) :
            window.__setattr__(f"category{i}", gf.load_py("renamer"))
            window.__getattribute__(f"category{i}").m_ui.category.setText(_files_names[i])
            window.__setattr__(f"categoryLayout{i}", QVBoxLayout())
            window.__getattribute__(f"categoryLayout{i}").setObjectName(f"categoryLayout{i}")
            for j in range(len(_files_sorted[i])) :
                window.__setattr__(f"category{i}-{j}", gf.load_py("renamer"))
                if j%2 == 0 :
                    window.__getattribute__(f"category{i}-{j}").m_ui.evenOldName.setText(_files_sorted[i][j]['original'])
                    window.__getattribute__(f"category{i}-{j}").m_ui.evenNewName.setText(_files_sorted[i][j]['final'])
                    window.__getattribute__(f"category{i}-{j}").m_ui.evenNewName.textChanged.connect(lambda _, i=i, j=j :  window.categoryInputs[i][j].setText(_) ) # set_in_2D_list("categoryInputs", i, j, _)) 
                    window.__getattribute__(f"categoryLayout{i}").addWidget(window.__getattribute__(f"category{i}-{j}").m_ui.evenContainer) 
                else :
                    window.__getattribute__(f"category{i}-{j}").m_ui.oddOldName.setText(_files_sorted[i][j]['original'])
                    window.__getattribute__(f"category{i}-{j}").m_ui.oddNewName.setText(_files_sorted[i][j]['final'])
                    window.__getattribute__(f"category{i}-{j}").m_ui.oddNewName.textChanged.connect(lambda _, i=i, j=j :  window.categoryInputs[i][j].setText(_) ) # set_in_2D_list("categoryInputs", i, j, _)) 
                    window.__getattribute__(f"categoryLayout{i}").addWidget(window.__getattribute__(f"category{i}-{j}").m_ui.oddContainer) 
            window.__getattribute__(f'category{i}').m_ui.categoryLayout.addLayout(window.__getattribute__(f'categoryLayout{i}'))
            window.__getattribute__(f"category{i}").m_ui.category.setText(_files_names[i])
            window.__getattribute__(f"category{i}").m_ui.category.textChanged.connect(lambda _, i=i : window.categoriesNamesInputs[i].setText(_) ) # set_in_list("categoriesNamesInputs", i, _)) 
            window.__getattribute__(f"category{i}").m_ui.refresh.clicked.connect(lambda _=0, i=i : refresh_data(i))
            window.m_ui.scrollLayout.addWidget(window.__getattribute__(f'category{i}').m_ui.categoryGroup)
        
        # window.m_ui.statusbar.removeWidget(window.renamer.m_ui.loadSpinner)
        # window.m_ui.statusbar.addWidget(window.renamer.m_ui.completedMessage)
        # time.sleep(10)
        # window.m_ui.statusbar.removeWidget(window.renamer.m_ui.completedMessage)
        
    def set_in_2D_list(_list: list, _first_index : int, _second_index : int, _value : any) :
        """Set the value at the index in a specific list of window

        Args:
            _list (list): The name of the list in window
            _first_index (int): The first index in the first dimension
            _second_index (int): The second index in the second dimension
            _value (any): The value to set
        """
        window.__getattribute__(_list)[_first_index][_second_index] = _value
        
    def set_in_list(_list: list, _index : int, _value : any) :
        """Set the value at the index in a specific list of window

        Args:
            _list (list): The name of the list in window
            _index (int): The index where to set
            _value (any): The value to set
        """
        window.__getattribute__(_list)[_index] = _value        
        
    def refresh_data(_index : int) :
        
        print(_index, window.categoryInputs[_index][j].text())
        # print(_index, window.categoriesNamesInputs[_index])
        if window.filesNames[_index] != window.categoriesNamesInputs[_index].text() :
            categoryObject = gf.get_episode_object(window.categoriesNamesInputs[_index].text(), True)
            set_in_list("filesNames", _index, categoryObject["name"])
            window.__setattr__(f"categoryLayout{_index}", QVBoxLayout())
            window.__getattribute__(f"categoryLayout{_index}").setObjectName(f"categoryLayout{_index}")
            for j in range(len(window.categoryInputs[_index])) :
                fileObject = gf.get_episode_object(window.categoryInputs[_index][j].text())
                fileObject["name"] = categoryObject["name"]
                if categoryObject["season"] != 0 :
                    fileObject["season"] = categoryObject["season"]
                if categoryObject["year"] != None :
                    fileObject["year"] = categoryObject["year"]
                if categoryObject["type"] != 0 :
                    fileObject["type"] = categoryObject["type"]
                fileObject["final"] = gf.get_name_from_object(fileObject)
                window.categoryInputs[_index][j].setText(fileObject["final"])
                # set_in_2D_list("categoryInputs", _index, j, fileObject["final"])
                set_in_2D_list("filesObjects", _index, j, fileObject)
                
                print(window.categoryInputs[_index][j].text())
                # print(window.__getattribute__(f'categoryLayout{_index}').count())
                # print(j, window.__getattribute__(f"category{_index}-{j}").m_ui.evenNewName.text())
                # gf.clear_layout(window.__getattribute__(f'category{_index}').m_ui.categoryLayout)
                # print(fileObject)
                
                # if j%2 == 0 :
                    # print('even')
                    # window.__getattribute__(f"category{_index}-{j}").m_ui.evenNewName.setText(fileObject['final'])
                # else :
                    # print('odd')
                    # window.__getattribute__(f"category{_index}-{j}").m_ui.oddNewName.setText(fileObject['final'])
                
            #     window.__setattr__(f"category{_index}-{j}", gf.load_py("renamer"))
            #     if j%2 == 0 :
            #         window.__getattribute__(f"category{_index}-{j}").m_ui.evenOldName.setText(fileObject['original'])
            #         window.__getattribute__(f"category{_index}-{j}").m_ui.evenNewName.setText(fileObject['final'])
            #         window.__getattribute__(f"category{_index}-{j}").m_ui.evenNewName.textChanged.connect(lambda _, i=_index, j=j :   set_in_2D_list("categoryInputs", i, j, _)) 
            #         window.__getattribute__(f"categoryLayout{_index}").addWidget(window.__getattribute__(f"category{_index}-{j}").m_ui.evenContainer) 
            #     else :
            #         window.__getattribute__(f"category{_index}-{j}").m_ui.oddOldName.setText(fileObject['original'])
            #         window.__getattribute__(f"category{_index}-{j}").m_ui.oddNewName.setText(fileObject['final'])
            #         window.__getattribute__(f"category{_index}-{j}").m_ui.oddNewName.textChanged.connect(lambda _, i=_index, j=j : set_in_2D_list("categoryInputs", i, j, _)) 
            #         window.__getattribute__(f"categoryLayout{_index}").addWidget(window.__getattribute__(f"category{_index}-{j}").m_ui.oddContainer) 
            # gf.clear_layout(window.__getattribute__(f'category{_index}').m_ui.categoryLayout)
            # window.__getattribute__(f'category{_index}').m_ui.categoryLayout.addLayout(window.__getattribute__(f'categoryLayout{_index}'))
            
            # showFiles(window.filesNames, window.filesObjects)
        # else :
        #     for j in len(window.categoryInputs[_index]) :
        #         fileObject = gf.get_episode_object(window.categoryInputs[_index][j])
        
        # print(_index, window.categoriesNamesInputs[_index])
        # print(_index, window.categoryInputs[_index])
        # print(window.category0.m_ui.category.text())
        
    def refresh_datas() :
        print(window.filesNames)
    
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