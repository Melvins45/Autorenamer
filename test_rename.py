import pytest
import os
from PySide2.QtCore import Qt, QRegExp
from PySide2.QtWidgets import QWidget

def test_rename(main, qtbot) :
    # Take a pathFolder for the test
    # test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life"
    # test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life - Copie (4)"
    test_folder = r"C:\Users\user\Downloads\Telegram Desktop\a - Copie"
    result_files = len(os.listdir(test_folder))
    
    # Try to rename
    main.m_ui.folderNameEdit.setText(test_folder)
    qtbot.mouseClick(main.m_ui.parcourirButton, Qt.LeftButton)
    main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"category").setText( main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"category").text() + " 1 VOSTFR " )
    qtbot.mouseClick(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"refresh"), Qt.LeftButton)
    qtbot.mouseClick(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget, "renameAll"), Qt.LeftButton)
    
    # Verify
    print(os.listdir(test_folder))
    assert os.listdir(test_folder)[0] == "Heaven Official Blessing S01 EP12 VOSTFR.mp4"
    
def test_create_folder(main, qtbot) :
    # Take a pathFolder for the test
    # test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life"
    # test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life - Copie (4)"
    test_folder = r"C:\Users\user\Downloads\Telegram Desktop\a - Copie (2)"
    result_files = len(os.listdir(test_folder))
    
    # Try to rename and create folder
    main.m_ui.folderNameEdit.setText(test_folder)
    qtbot.mouseClick(main.m_ui.parcourirButton, Qt.LeftButton)
    main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"category").setText(" " + main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"category").text() + " S1 VOSTFR " )
    qtbot.mouseClick(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"refresh"), Qt.LeftButton)
    qtbot.mouseClick(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"createNewFolder"), Qt.LeftButton)
    qtbot.mouseClick(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget, "renameAll"), Qt.LeftButton)
    
    # Verify
    # print(os.listdir(test_folder))
    assert os.listdir(test_folder)[0] == " Heaven Official Blessing S1 VOSTFR"
    assert os.listdir(os.path.join(test_folder, os.listdir(test_folder)[0]))[0] == "Heaven Official Blessing S01 EP12 VOSTFR.mp4"
    
def test_divide_by_seasons(main, qtbot) :
    # Take a pathFolder for the test
    # test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life"
    # test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life - Copie (4)"
    test_folder = r"C:\Users\user\Downloads\Telegram Desktop\a - Copie (3)"
    result_files = len(os.listdir(test_folder))
    
    # Try to rename and create folder
    main.m_ui.folderNameEdit.setText(test_folder)
    qtbot.mouseClick(main.m_ui.parcourirButton, Qt.LeftButton)
    main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"category").setText(" " + main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"category").text() + " S1 VOSTFR " )
    qtbot.mouseClick(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"refresh"), Qt.LeftButton)
    qtbot.mouseClick(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"divideBySeasons"), Qt.LeftButton)
    qtbot.mouseClick(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget, "renameAll"), Qt.LeftButton)
    
    # Verify
    # print(os.listdir(test_folder))
    assert os.listdir(test_folder)[0] == "S01"
    assert os.listdir(os.path.join(test_folder, os.listdir(test_folder)[0]))[0] == "Heaven Official Blessing S01 EP12 VOSTFR.mp4"
    
def test_create_folder_and_divide_by_seasons(main, qtbot) :
    # Take a pathFolder for the test
    # test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life"
    # test_folder = r"C:\Users\user\Downloads\Telegram Desktop\Cheat Kusushi No Slow Life - Copie (4)"
    test_folder = r"C:\Users\user\Downloads\Telegram Desktop\a - Copie (4)"
    result_files = len(os.listdir(test_folder))
    
    # Try to rename and create folder
    main.m_ui.folderNameEdit.setText(test_folder)
    qtbot.mouseClick(main.m_ui.parcourirButton, Qt.LeftButton)
    main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"category").setText(" " + main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"categoryEntity").findChild(QWidget,"categoryContainer").findChild(QWidget,"category").text() + " S1 VOSTFR " )
    qtbot.mouseClick(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"refresh"), Qt.LeftButton)
    qtbot.mouseClick(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"createNewFolder"), Qt.LeftButton)
    qtbot.mouseClick(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget,"divideBySeasons"), Qt.LeftButton)
    qtbot.mouseClick(main.m_ui.scrollLayout.itemAt(0).widget().findChild(QWidget, "renameAll"), Qt.LeftButton)
    
    # Verify
    # print(os.listdir(test_folder))
    assert os.listdir(test_folder)[0] == " Heaven Official Blessing S1 VOSTFR"
    assert os.listdir(os.path.join(test_folder, os.listdir(test_folder)[0]))[0] == "S01"
    assert os.listdir( os.path.join(test_folder, os.listdir(test_folder)[0], os.listdir(os.path.join(test_folder, os.listdir(test_folder)[0]))[0]) )[0] == "Heaven Official Blessing S01 EP12 VOSTFR.mp4"