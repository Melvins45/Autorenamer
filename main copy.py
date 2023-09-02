from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QFile, QTextStream, QIODevice, Signal, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QResizeEvent)
from PySide2.QtWidgets import *
import sys, os, re
import constants as gc
import helpers as gf
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

actualPage = list(gc.PAGES_TITLES.keys())[0]

class ClassWindow(QMainWindow):
    resized = Signal( QResizeEvent )
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        if self.objectName():
            self.setObjectName(list(gc.PAGES_TITLES.values())[0])
        self.resize(678, 497)
        icon = QIcon()
        icon.addFile(resource_path(u"img\\template_icon.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
        
    def resizeEvent(self, event: QResizeEvent) -> None:
        self.resized.emit(event)
        return super(ClassWindow, self).resizeEvent(event)

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("CallmeBack", u"MainWindow", None))
    # retranslateUi
    

if __name__ == "__main__":
    styleSheetFile = QFile( resource_path("style.qss") )
    styleSheetFile.open(QIODevice.ReadOnly)
    styleSheet = QTextStream(styleSheetFile).readAll()
    form = QApplication(sys.argv)
    fontDatabase = QFontDatabase()
    fontDatabase.addApplicationFont(resource_path("fonts\\inder.ttf"))
    form.setFont(QFont(fontDatabase.applicationFontFamilies(0)[0], 10))
    form.setStyleSheet(styleSheet)
    window = gf.load_py("home") #ClassWindow() #gf.load_ui("window")
    #window.setWindowTitle( QCoreApplication.translate("Template", "Template", None) )
    
    def activePage(page: str) :
        match page :
            case "template" :
                print(window.__getattribute__(page).m_ui.plainTextEdit.toPlainText())
            case _ :
                print(window.__getattribute__(page).m_ui.plainTextEdit.toPlainText())
    
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
    window.__setattr__("renamerr", gf.load_py("renamer"))
    # window.m_ui.scrollArea.addWidget(window.renamer.m_ui.categoryGroup)
    
    # window.m_ui.scrollLayout.addWidget(window.renamer.m_ui.Awidget)
    # window.m_ui.scrollLayout.addWidget(window.renamerr.m_ui.categoryGroup)
    
    # window.__setattr__("scrollAreaContent", QWidget())
    # window.scrollAreaContent.setObjectName(u"scrollAreaContent")
    # window.scrollAreaContent.setGeometry(QRect(0, 0, 643, 329))
    # window.__setattr__("scrollLayout2", QVBoxLayout(window.scrollAreaContent))
    # window.scrollLayout2.setObjectName(u"scrollLayout2")
    # window.scrollLayout2.addWidget(window.renamer.m_ui.Awidget)
    # window.scrollLayout2.addWidget(window.renamer.m_ui.categoryGroup)
    # window.scrollLayout2.setStretch(1, 1)
    for i in range(1,5):
            window.__setattr__(f"object{i}", gf.load_py("renamer"))
            window.m_ui.scrollLayout.addWidget(window.__getattribute__(f'object{i}').m_ui.categoryGroup)
    # window.scrollAreaContent.setLayout(window.scrollLayout2)
    # window.m_ui.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    # window.m_ui.scrollArea.setWidgetResizable(True)
    # window.m_ui.scrollArea.setWidget(window.scrollAreaContent)
    # window.__setattr__("renamer", gf.load_py("renamer"))
    # window.home.m_ui.
    
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