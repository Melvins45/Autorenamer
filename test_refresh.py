import pytest
import os
from time import sleep
from PySide2.QtCore import Qt, QRegExp
from PySide2.QtWidgets import QWidget

def test_refresh(main, qtbot) :
    # Take a pathFolder for the test
    # test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life"
    # test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life - Copie (4)"
    test_folder = r"C:\Users\user\Downloads\Telegram Desktop\a"
    result_files = len(os.listdir(test_folder))
    
    # Try to refresh
    main.m_ui.folderNameEdit.setText(test_folder)
    qtbot.mouseClick(main.m_ui.parcourirButton, Qt.LeftButton)
    main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"category").setText( main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"category").text() + " 3 VOSTFR " )
    qtbot.mouseClick(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"refresh"), Qt.LeftButton)
    
    # Verify
    assert main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget, "categoryEntity").findChild(QWidget, "inputContainer0").findChild(QWidget, "inputName").text() == "Heaven Official Blessing S03 EP12 VOSTFR.mp4" # main.filesObjects[0][0]["final"]