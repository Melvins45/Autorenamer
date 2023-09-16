import pytest
import os
from time import sleep
from PySide2.QtCore import Qt, QRegExp
from PySide2.QtWidgets import QWidget

def test_browse(main, qtbot) :
    # test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life"
    # test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life - Copie (4)"
    test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life - Copie (5)"
    result_files = len(os.listdir(test_folder))
    
    print( [ (main.m_ui.scrollLayout.itemAt(i), i) for i in range(2) ] )
    
    # qtbot.keyClick(main.m_ui.folderNameEdit, test_folder)
    main.m_ui.folderNameEdit.setText(test_folder)
    main.m_ui.parcourirButton.click()
    # qtbot.mouseClick(main.m_ui.parcourirButton, Qt.LeftButton)
    
    # print( [ (main.m_ui.scrollArea.children(), i) for i in range(len(main.filesObjects)) ] )
    # print( [ (main.m_ui.scrollAreaWidgetContents.children(), i) for i in range(len(main.filesObjects)) ] )
    print( [ (main.scroll_item(i), i) for i in range(len(main.filesObjects)) ] )
    print( [ (main.m_ui.scrollLayout.itemAt(i), i) for i in range(len(main.filesObjects)) ] )
    # sum([ len(i) for i in main.filesObjects ])
    # len(main.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"categoryEntity").findChildren(QWidget, "^inputContainer")) for i in range(len(main.filesObjects))
    
    # sleep(5)
    # while not main.hadShownAll :
    #     assert main.m_ui.folderName.text() == "Nom du dossier"
    #     if main.hadShownAll :
    #         assert sum([ len(main.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"categoryEntity").findChildren(QWidget, QRegExp(r"^inputContainer\d+$"))) for i in range(len(main.filesObjects)) ]) == result_files
    assert sum([ len(main.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"categoryEntity").findChildren(QWidget, QRegExp(r"^inputContainer\d+$"))) for i in range(len(main.filesObjects)) ]) == result_files
    # assert sum([ len(i) for i in main.filesObjects ]) == result_files