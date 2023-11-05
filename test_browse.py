import pytest
import os
from PySide2.QtCore import Qt, QRegExp
from PySide2.QtWidgets import QWidget

def test_browse(main, qtbot) :
    # Take a pathFolder for the test
    # test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life"
    # test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life - Copie (4)"
    test_folder = r"C:\Users\user\Downloads\Telegram Desktop\a"
    result_files = len(os.listdir(test_folder))
    
    # Try to browse
    main.m_ui.folderNameEdit.setText(test_folder)
    qtbot.mouseClick(main.m_ui.parcourirButton, Qt.LeftButton)
    
    # Verify
    i = 0
    sumOfInputNames = 0
    while main.m_ui.scrollLayout.itemAt(i) != None :
        sumOfInputNames += len(main.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"categoryEntity").findChildren(QWidget, QRegExp(r"^inputContainer\d+$")))
        i+=1
    assert sumOfInputNames == result_files
    # assert sum([ len(main.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"categoryEntity").findChildren(QWidget, QRegExp(r"^inputContainer\d+$"))) for i in range(10000) if main.m_ui.scrollLayout.itemAt(i) != None ]) == result_files
    # assert sum([ len(main.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"categoryEntity").findChildren(QWidget, QRegExp(r"^inputContainer\d+$"))) for i in range(10000) if main.m_ui.scrollLayout.itemAt(i) != None ]) == result_files
    # assert sum([ len(main.m_ui.scrollLayout.itemAt(i).widget().findChild(QWidget,"categoryEntity").findChildren(QWidget, QRegExp(r"^inputContainer\d+$"))) for i in range(len(main.filesObjects)) ]) == result_files