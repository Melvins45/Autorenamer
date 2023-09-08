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
                    window.__getattribute__(f"categoryLayout{i}").addWidget(window.__getattribute__(f"category{i}-{j}").m_ui.evenContainer) 
                else :
                    window.__getattribute__(f"category{i}-{j}").m_ui.oddOldName.setText(_files_sorted[i][j]['original'])
                    # window.__getattribute__(f"category{i}-{j}").m_ui.oddNewName.setText(_files_sorted[i][j]['final'])
                    # window.__getattribute__(f"categoryLayout{i}").addWidget(window.__getattribute__(f"category{i}-{j}").m_ui.oddContainer) 
            # window.__setattr__(f"filesIndex{i}", i)
            # window.__setattr__(f"refresh_it{i}", lambda _=0, i=i : print(i) ) #refresh_data(window.__getattribute__(f'filesIndex{i}')))
            # refresh_it = lambda : refresh_data(window.__getattribute__(f'filesIndex{i}'))
            window.__getattribute__(f'category{i}').m_ui.categoryLayout.addLayout(window.__getattribute__(f'categoryLayout{i}'))
            window.__getattribute__(f"category{i}").m_ui.category.setText(_files_names[i])
            # window.__setattr__(f"refresher{i}", QPushButton(None, 'Refresh'))
            # window.__getattribute__(f"refresher{i}").setObjectName(f"refresher{i}")
            # window.__getattribute__(f"refresher{i}").clicked.connect(lambda : refresh_data(i))
            # window.__getattribute__(f"category{i}").m_ui.categoryMenu.addWidget(window.__getattribute__(f"refresher{i}"), 2)
            window.__getattribute__(f"category{i}").m_ui.refresh.clicked.connect(lambda _=0, i=i : refresh_data(i))
            window.m_ui.scrollLayout.addWidget(window.__getattribute__(f'category{i}').m_ui.categoryGroup)
        
        # window.m_ui.statusbar.removeWidget(window.renamer.m_ui.loadSpinner)
        # window.m_ui.statusbar.addWidget(window.renamer.m_ui.completedMessage)
        # time.sleep(10)
        # window.m_ui.statusbar.removeWidget(window.renamer.m_ui.completedMessage)
        
    def refresh_data(_index : int) :
        print(_index, window.__getattribute__(f"category{_index}").m_ui.category.text())
        print(window.category0.m_ui.category.text())
        
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