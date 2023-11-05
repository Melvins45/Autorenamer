import pytest
import os
from PySide2.QtCore import Qt, QRegExp
from PySide2.QtWidgets import QWidget

def test_integration_do_all(main, qtbot) :
    # Take a pathFolder for the test
    # test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life"
    # test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life - Copie (4)"
    test_folder = r"C:\Users\user\Downloads\Telegram Desktop\a - Copie (5)"
    result_files = len(os.listdir(test_folder))
    
    # Browse a folder
    main.m_ui.folderNameEdit.setText(test_folder)
    qtbot.mouseClick(main.m_ui.parcourirButton, Qt.LeftButton)
    
    # Save previous datas
    previousNumberOfCategories = 0
    while main.m_ui.scrollLayout.itemAt(previousNumberOfCategories) != None :
        previousNumberOfCategories += 1
    previousNumberOfInputsNamesInCategories0And1 = [ len(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"categoryEntity").findChildren(QWidget, QRegExp(r"^inputContainer\d+$"))), len(main.m_ui.scrollLayout.itemAt(1).widget().findChild(QWidget,"categoryEntity").findChildren(QWidget, QRegExp(r"^inputContainer\d+$"))) ]
    
    # Try to fuse a category with another
    qtbot.mouseClick(main.m_ui.scrollLayout.itemAt(1).widget().findChild(QWidget,"fuseWith"), Qt.LeftButton)
    qtbot.mouseClick(main.fuser.m_ui.scrollLayout.itemAt(0).widget(), Qt.LeftButton)
    qtbot.mouseClick(main.fuser.m_ui.ok, Qt.LeftButton)
    main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"category").setText( main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"category").text() + " S1 VOSTFR " )
    qtbot.mouseClick(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"refresh"), Qt.LeftButton)
    qtbot.mouseClick(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"createNewFolder"), Qt.LeftButton)
    qtbot.mouseClick(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"renameAll"), Qt.LeftButton)
    
    # Verify
    actualNumberOfCategories = 0
    while main.m_ui.scrollLayout.itemAt(actualNumberOfCategories) != None :
        actualNumberOfCategories += 1
    actualNumberOfInputsNamesInCategory0 = len(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"categoryEntity").findChildren(QWidget, QRegExp(r"^inputContainer\d+$")))
    assert previousNumberOfCategories == actualNumberOfCategories + 1
    assert actualNumberOfInputsNamesInCategory0 == sum(previousNumberOfInputsNamesInCategories0And1)
    assert os.listdir(test_folder)[0] == "Heaven Official Blessing S1 VOSTFR"
    assert os.listdir(os.path.join(test_folder, os.listdir(test_folder)[0]))[0] == "Heaven Official Blessing S01 EP07 VOSTFR.flv"
    
def test_integration_without_create_folder(main, qtbot) :
    # Take a pathFolder for the test
    # test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life"
    # test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life - Copie (4)"
    test_folder = r"C:\Users\user\Downloads\Telegram Desktop\a - Copie (6)"
    result_files = len(os.listdir(test_folder))
    
    # Browse a folder
    main.m_ui.folderNameEdit.setText(test_folder)
    qtbot.mouseClick(main.m_ui.parcourirButton, Qt.LeftButton)
    
    # Save previous datas
    previousNumberOfCategories = 0
    while main.m_ui.scrollLayout.itemAt(previousNumberOfCategories) != None :
        previousNumberOfCategories += 1
    previousNumberOfInputsNamesInCategories0And1 = [ len(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"categoryEntity").findChildren(QWidget, QRegExp(r"^inputContainer\d+$"))), len(main.m_ui.scrollLayout.itemAt(1).widget().findChild(QWidget,"categoryEntity").findChildren(QWidget, QRegExp(r"^inputContainer\d+$"))) ]
    
    # Try to fuse a category with another
    qtbot.mouseClick(main.m_ui.scrollLayout.itemAt(1).widget().findChild(QWidget,"fuseWith"), Qt.LeftButton)
    qtbot.mouseClick(main.fuser.m_ui.scrollLayout.itemAt(0).widget(), Qt.LeftButton)
    qtbot.mouseClick(main.fuser.m_ui.ok, Qt.LeftButton)
    main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"category").setText( main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"category").text() + " S1 VOSTFR " )
    qtbot.mouseClick(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"refresh"), Qt.LeftButton)
    qtbot.mouseClick(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"renameAll"), Qt.LeftButton)
    
    # Verify
    actualNumberOfCategories = 0
    while main.m_ui.scrollLayout.itemAt(actualNumberOfCategories) != None :
        actualNumberOfCategories += 1
    actualNumberOfInputsNamesInCategory0 = len(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"categoryEntity").findChildren(QWidget, QRegExp(r"^inputContainer\d+$")))
    assert previousNumberOfCategories == actualNumberOfCategories + 1
    assert actualNumberOfInputsNamesInCategory0 == sum(previousNumberOfInputsNamesInCategories0And1)
    assert os.listdir(test_folder)[0] == "Heaven Official Blessing S01 EP07 VOSTFR.flv"