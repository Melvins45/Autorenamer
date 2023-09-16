import pytest
import os
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget

def test_close(main, qtbot) :
    # Take a pathFolder for the test
    # test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life"
    # test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life - Copie (4)"
    test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life - Copie (4)"
    result_files = len(os.listdir(test_folder))
    
    # Browse the test's folder
    main.m_ui.folderNameEdit.setText(test_folder)
    qtbot.mouseClick(main.m_ui.parcourirButton, Qt.LeftButton)
    
    # Save previous datas
    previousNumberOfCategories = 0
    while main.m_ui.scrollLayout.itemAt(previousNumberOfCategories) != None :
        previousNumberOfCategories += 1
        
    # Try to close
    qtbot.mouseClick(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"close"), Qt.LeftButton)
    
    # Verify
    actualNumberOfCategories = 0
    while main.m_ui.scrollLayout.itemAt(actualNumberOfCategories) != None :
        actualNumberOfCategories += 1
    assert previousNumberOfCategories == actualNumberOfCategories + 1