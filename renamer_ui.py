# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'renamer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icon_rc
import loader_rc

class Ui_home(object):
    def setupUi(self, home):
        if not home.objectName():
            home.setObjectName(u"home")
        home.resize(1220, 571)
        icon = QIcon()
        icon.addFile(u":/newPrefix/template_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        home.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(home)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Awidget = QWidget(home)
        self.Awidget.setObjectName(u"Awidget")
        self.Awidget.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 242, 175);")
        self.categoryGroup = QWidget(self.Awidget)
        self.categoryGroup.setObjectName(u"categoryGroup")
        self.categoryGroup.setGeometry(QRect(30, 30, 511, 281))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoryGroup.sizePolicy().hasHeightForWidth())
        self.categoryGroup.setSizePolicy(sizePolicy)
        self.categoryGroup.setMinimumSize(QSize(0, 0))
        self.categoryGroup.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout_5 = QHBoxLayout(self.categoryGroup)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.categoryEntity = QWidget(self.categoryGroup)
        self.categoryEntity.setObjectName(u"categoryEntity")
        self.categoryEntity.setStyleSheet(u"")
        self.categoryLayout = QVBoxLayout(self.categoryEntity)
        self.categoryLayout.setSpacing(0)
        self.categoryLayout.setObjectName(u"categoryLayout")
        self.categoryLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.categoryLayout.setContentsMargins(0, 0, 0, 0)
        self.categoryContainer = QWidget(self.categoryEntity)
        self.categoryContainer.setObjectName(u"categoryContainer")
        self.categoryContainer.setStyleSheet(u"background-color: rgb(217, 217, 217);\n"
"border: none;\n"
"border-top-right-radius: 16%;\n"
"border-top-left-radius: 16%;")
        self.horizontalLayout_6 = QHBoxLayout(self.categoryContainer)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.category = QLineEdit(self.categoryContainer)
        self.category.setObjectName(u"category")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(12)
        sizePolicy1.setVerticalStretch(32)
        sizePolicy1.setHeightForWidth(self.category.sizePolicy().hasHeightForWidth())
        self.category.setSizePolicy(sizePolicy1)
        self.category.setMinimumSize(QSize(0, 70))
        font = QFont()
        font.setPointSize(16)
        self.category.setFont(font)
        self.category.setStyleSheet(u"border: none;\n"
"border-top-left-radius: 16%;\n"
"background: transparent;")
        self.category.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.category)

        self.close = QPushButton(self.categoryContainer)
        self.close.setObjectName(u"close")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.close.sizePolicy().hasHeightForWidth())
        self.close.setSizePolicy(sizePolicy2)
        self.close.setMinimumSize(QSize(0, 70))
        self.close.setStyleSheet(u"border: none;\n"
"border-top-left-radius: 0%;\n"
"border-left: 1px solid rgb(0,0,0);\n"
"margin: 15% 0px;\n"
"background : transparent;")

        self.horizontalLayout_6.addWidget(self.close)

        self.horizontalLayout_6.setStretch(0, 7)
        self.horizontalLayout_6.setStretch(1, 1)

        self.categoryLayout.addWidget(self.categoryContainer)


        self.horizontalLayout_5.addWidget(self.categoryEntity)

        self.categoryMenu = QVBoxLayout()
        self.categoryMenu.setObjectName(u"categoryMenu")
        self.refresh = QPushButton(self.categoryGroup)
        self.refresh.setObjectName(u"refresh")
        sizePolicy2.setHeightForWidth(self.refresh.sizePolicy().hasHeightForWidth())
        self.refresh.setSizePolicy(sizePolicy2)
        self.refresh.setFont(font)
        self.refresh.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"border: none;\n"
"border-radius: 15%;padding: 5%;")

        self.categoryMenu.addWidget(self.refresh)

        self.renameAll = QPushButton(self.categoryGroup)
        self.renameAll.setObjectName(u"renameAll")
        sizePolicy2.setHeightForWidth(self.renameAll.sizePolicy().hasHeightForWidth())
        self.renameAll.setSizePolicy(sizePolicy2)
        self.renameAll.setFont(font)
        self.renameAll.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"border: none;\n"
"border-radius: 15%;padding: 5%;")

        self.categoryMenu.addWidget(self.renameAll)

        self.fuseWith = QPushButton(self.categoryGroup)
        self.fuseWith.setObjectName(u"fuseWith")
        sizePolicy2.setHeightForWidth(self.fuseWith.sizePolicy().hasHeightForWidth())
        self.fuseWith.setSizePolicy(sizePolicy2)
        self.fuseWith.setFont(font)
        self.fuseWith.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"border: none;\n"
"border-radius: 15%;padding: 5%;")

        self.categoryMenu.addWidget(self.fuseWith)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.createNewFolder = QCheckBox(self.categoryGroup)
        self.createNewFolder.setObjectName(u"createNewFolder")
        self.createNewFolder.setFont(font)

        self.verticalLayout_4.addWidget(self.createNewFolder)

        self.createNewFolderFollow = QPushButton(self.categoryGroup)
        self.createNewFolderFollow.setObjectName(u"createNewFolderFollow")
        self.createNewFolderFollow.setFont(font)
        self.createNewFolderFollow.setStyleSheet(u"border: none;")

        self.verticalLayout_4.addWidget(self.createNewFolderFollow)


        self.categoryMenu.addLayout(self.verticalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.categoryMenu.addItem(self.verticalSpacer)


        self.horizontalLayout_5.addLayout(self.categoryMenu)

        self.horizontalLayout_5.setStretch(0, 1)
        self.oddContainer = QWidget(self.Awidget)
        self.oddContainer.setObjectName(u"oddContainer")
        self.oddContainer.setGeometry(QRect(310, 380, 351, 61))
        self.oddContainer.setMinimumSize(QSize(0, 50))
        self.oddContainer.setStyleSheet(u"border: none;")
        self.horizontalLayout_4 = QHBoxLayout(self.oddContainer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.oddOldName = QLabel(self.oddContainer)
        self.oddOldName.setObjectName(u"oddOldName")
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.oddOldName.sizePolicy().hasHeightForWidth())
        self.oddOldName.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setPointSize(14)
        font1.setStrikeOut(True)
        self.oddOldName.setFont(font1)
        self.oddOldName.setStyleSheet(u"text-decoration: line-through;")
        self.oddOldName.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.oddOldName.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.oddOldName)

        self.oddNewName = QLineEdit(self.oddContainer)
        self.oddNewName.setObjectName(u"oddNewName")
        font2 = QFont()
        font2.setPointSize(14)
        self.oddNewName.setFont(font2)
        self.oddNewName.setStyleSheet(u"border: none;\n"
"background: transparent;")

        self.horizontalLayout_4.addWidget(self.oddNewName)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.evenContainer = QWidget(self.Awidget)
        self.evenContainer.setObjectName(u"evenContainer")
        self.evenContainer.setGeometry(QRect(10, 420, 301, 51))
        self.evenContainer.setMinimumSize(QSize(0, 50))
        self.evenContainer.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.horizontalLayout_2 = QHBoxLayout(self.evenContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.evenOldName = QLabel(self.evenContainer)
        self.evenOldName.setObjectName(u"evenOldName")
        sizePolicy3.setHeightForWidth(self.evenOldName.sizePolicy().hasHeightForWidth())
        self.evenOldName.setSizePolicy(sizePolicy3)
        self.evenOldName.setFont(font1)
        self.evenOldName.setStyleSheet(u"text-decoration: line-through;")
        self.evenOldName.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.evenOldName.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.evenOldName)

        self.evenNewName = QLineEdit(self.evenContainer)
        self.evenNewName.setObjectName(u"evenNewName")
        self.evenNewName.setFont(font2)
        self.evenNewName.setStyleSheet(u"border: none;\n"
"background: transparent;")

        self.horizontalLayout_2.addWidget(self.evenNewName)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.loadSpinner = QWidget(self.Awidget)
        self.loadSpinner.setObjectName(u"loadSpinner")
        self.loadSpinner.setGeometry(QRect(400, 470, 150, 25))
        self.loadSpinner.setMinimumSize(QSize(0, 0))
        self.loadSpinner.setMaximumSize(QSize(150, 25))
        self.horizontalLayout = QHBoxLayout(self.loadSpinner)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.loader = QLabel(self.loadSpinner)
        self.loader.setObjectName(u"loader")
        self.loader.setMaximumSize(QSize(20, 16777215))
        self.loader.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.loader)

        self.operating = QLabel(self.loadSpinner)
        self.operating.setObjectName(u"operating")
        sizePolicy3.setHeightForWidth(self.operating.sizePolicy().hasHeightForWidth())
        self.operating.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setPointSize(14)
        font3.setItalic(True)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        self.operating.setFont(font3)
        self.operating.setStyleSheet(u"text-decoration: none;font-style: italic;")
        self.operating.setAlignment(Qt.AlignCenter)
        self.operating.setWordWrap(False)

        self.horizontalLayout.addWidget(self.operating)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.completedMessage = QWidget(self.Awidget)
        self.completedMessage.setObjectName(u"completedMessage")
        self.completedMessage.setGeometry(QRect(430, 510, 150, 25))
        self.completedMessage.setMinimumSize(QSize(0, 0))
        self.completedMessage.setMaximumSize(QSize(150, 25))
        self.horizontalLayout_3 = QHBoxLayout(self.completedMessage)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.okIcon = QLabel(self.completedMessage)
        self.okIcon.setObjectName(u"okIcon")
        self.okIcon.setMaximumSize(QSize(20, 20))
        self.okIcon.setStyleSheet(u"border-image: url(:/icon/images/ok.png);")

        self.horizontalLayout_3.addWidget(self.okIcon)

        self.completedLabel = QLabel(self.completedMessage)
        self.completedLabel.setObjectName(u"completedLabel")
        sizePolicy3.setHeightForWidth(self.completedLabel.sizePolicy().hasHeightForWidth())
        self.completedLabel.setSizePolicy(sizePolicy3)
        self.completedLabel.setFont(font3)
        self.completedLabel.setStyleSheet(u"text-decoration: none;font-style: italic;")
        self.completedLabel.setAlignment(Qt.AlignCenter)
        self.completedLabel.setWordWrap(False)

        self.horizontalLayout_3.addWidget(self.completedLabel)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        self.pushButton = QPushButton(self.Awidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 350, 75, 23))
        self.pushButton.setStyleSheet(u"border: none;\n"
"border-left: 1px solid rgb(0,0,0);\n"
"margin: 5px 0px;")
        self.fuser = QWidget(self.Awidget)
        self.fuser.setObjectName(u"fuser")
        self.fuser.setGeometry(QRect(560, 40, 321, 301))
        self.fuser.setMinimumSize(QSize(321, 301))
        self.fuser.setMaximumSize(QSize(321, 301))
        self.fuser.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QVBoxLayout(self.fuser)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.fuserQuestion = QLabel(self.fuser)
        self.fuserQuestion.setObjectName(u"fuserQuestion")
        sizePolicy3.setHeightForWidth(self.fuserQuestion.sizePolicy().hasHeightForWidth())
        self.fuserQuestion.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setPointSize(14)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        self.fuserQuestion.setFont(font4)
        self.fuserQuestion.setStyleSheet(u"text-decoration: none;")
        self.fuserQuestion.setAlignment(Qt.AlignCenter)
        self.fuserQuestion.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.fuserQuestion)

        self.scrollArea = QScrollArea(self.fuser)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border: none;")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 303, 166))
        self.scrollLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollLayout.setObjectName(u"scrollLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.okLayout = QHBoxLayout()
        self.okLayout.setObjectName(u"okLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.okLayout.addItem(self.horizontalSpacer)

        self.ok = QPushButton(self.fuser)
        self.ok.setObjectName(u"ok")
        sizePolicy2.setHeightForWidth(self.ok.sizePolicy().hasHeightForWidth())
        self.ok.setSizePolicy(sizePolicy2)
        self.ok.setFont(font)
        self.ok.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"border: 1px solid black;\n"
"border-radius: 0%;padding: 5%;margin: 10% 0%;")

        self.okLayout.addWidget(self.ok)


        self.verticalLayout_2.addLayout(self.okLayout)

        self.categoryRadio = QRadioButton(self.Awidget)
        self.categoryRadio.setObjectName(u"categoryRadio")
        self.categoryRadio.setGeometry(QRect(600, 430, 171, 31))
        sizePolicy2.setHeightForWidth(self.categoryRadio.sizePolicy().hasHeightForWidth())
        self.categoryRadio.setSizePolicy(sizePolicy2)
        self.categoryRadio.setMinimumSize(QSize(0, 30))
        self.categoryRadio.setMaximumSize(QSize(20000, 40))
        self.categoryRadio.setStyleSheet(u"")
        self.fuserQuestion_2 = QLabel(self.Awidget)
        self.fuserQuestion_2.setObjectName(u"fuserQuestion_2")
        self.fuserQuestion_2.setGeometry(QRect(620, 380, 231, 21))
        sizePolicy3.setHeightForWidth(self.fuserQuestion_2.sizePolicy().hasHeightForWidth())
        self.fuserQuestion_2.setSizePolicy(sizePolicy3)
        self.fuserQuestion_2.setFont(font4)
        self.fuserQuestion_2.setStyleSheet(u"text-decoration: none;")
        self.fuserQuestion_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.fuserQuestion_2.setWordWrap(True)
        self.emptySearch = QWidget(self.Awidget)
        self.emptySearch.setObjectName(u"emptySearch")
        self.emptySearch.setGeometry(QRect(900, 160, 625, 311))
        self.emptySearch.setStyleSheet(u"border: 2px dashed; border-radius: 10%;\n"
"border-color: rgb(217, 217, 217);")
        self.verticalLayout_5 = QVBoxLayout(self.emptySearch)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.noFileFound = QLabel(self.emptySearch)
        self.noFileFound.setObjectName(u"noFileFound")
        font5 = QFont()
        font5.setFamily(u"MS Shell Dlg 2")
        font5.setPointSize(16)
        font5.setItalic(True)
        self.noFileFound.setFont(font5)
        self.noFileFound.setStyleSheet(u"border: none;\n"
"color: rgb(217, 217, 217);font-style: italic;")
        self.noFileFound.setAlignment(Qt.AlignCenter)
        self.noFileFound.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.noFileFound)


        self.verticalLayout.addWidget(self.Awidget)


        self.retranslateUi(home)
        self.createNewFolderFollow.clicked.connect(self.createNewFolder.animateClick)
        self.category.editingFinished.connect(self.refresh.animateClick)

        QMetaObject.connectSlotsByName(home)
    # setupUi

    def retranslateUi(self, home):
        home.setWindowTitle(QCoreApplication.translate("home", u"Template", None))
        self.category.setText(QCoreApplication.translate("home", u"Cat\u00e9gorie x", None))
        self.close.setText(QCoreApplication.translate("home", u"X", None))
        self.refresh.setText(QCoreApplication.translate("home", u"Rafra\u00eechir", None))
        self.renameAll.setText(QCoreApplication.translate("home", u"Tout renommer", None))
        self.fuseWith.setText(QCoreApplication.translate("home", u"Fusionner avec", None))
        self.createNewFolder.setText(QCoreApplication.translate("home", u"Cr\u00e9er un", None))
        self.createNewFolderFollow.setText(QCoreApplication.translate("home", u"   nouveau dossier", None))
        self.oddOldName.setText(QCoreApplication.translate("home", u"<html><head/><body><p>Ancien nom </p></body></html>", None))
        self.oddNewName.setText(QCoreApplication.translate("home", u"Nouveau nom", None))
        self.evenOldName.setText(QCoreApplication.translate("home", u"<html><head/><body><p>Ancien nom</p></body></html>", None))
        self.evenNewName.setText(QCoreApplication.translate("home", u"Nouveau nom", None))
        self.loader.setText("")
        self.operating.setText(QCoreApplication.translate("home", u"Chargement ...", None))
        self.okIcon.setText("")
        self.completedLabel.setText(QCoreApplication.translate("home", u"Termin\u00e9", None))
        self.pushButton.setText(QCoreApplication.translate("home", u"X", None))
        self.fuserQuestion.setText(QCoreApplication.translate("home", u"<html><head/><body><p>Avec quelle cat\u00e9gorie souhaitez-vous la fusionner ?</p></body></html>", None))
        self.ok.setText(QCoreApplication.translate("home", u"OK", None))
        self.categoryRadio.setText(QCoreApplication.translate("home", u"Category Name", None))
        self.fuserQuestion_2.setText(QCoreApplication.translate("home", u"<html><head/><body><p>CategoryName</p></body></html>", None))
        self.noFileFound.setText(QCoreApplication.translate("home", u"Aucune cat\u00e9gorie trouv\u00e9e ...", None))
    # retranslateUi

