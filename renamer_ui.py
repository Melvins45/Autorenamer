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
        home.resize(909, 541)
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
        self.categoryGroup.setGeometry(QRect(30, 30, 551, 331))
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
        self.categoryContainer.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.categoryContainer)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
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
        self.category.setStyleSheet(u"background-color: rgb(217, 217, 217);\n"
"border: none;\n"
"border-top-right-radius: 16%;\n"
"border-top-left-radius: 16%;")
        self.category.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.category)


        self.categoryLayout.addWidget(self.categoryContainer)


        self.horizontalLayout_5.addWidget(self.categoryEntity)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.renameAll_2 = QPushButton(self.categoryGroup)
        self.renameAll_2.setObjectName(u"renameAll_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.renameAll_2.sizePolicy().hasHeightForWidth())
        self.renameAll_2.setSizePolicy(sizePolicy2)
        self.renameAll_2.setFont(font)
        self.renameAll_2.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"border: none;\n"
"border-radius: 15%;padding: 5%;")

        self.verticalLayout_5.addWidget(self.renameAll_2)

        self.renameAll = QPushButton(self.categoryGroup)
        self.renameAll.setObjectName(u"renameAll")
        sizePolicy2.setHeightForWidth(self.renameAll.sizePolicy().hasHeightForWidth())
        self.renameAll.setSizePolicy(sizePolicy2)
        self.renameAll.setFont(font)
        self.renameAll.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"border: none;\n"
"border-radius: 15%;padding: 5%;")

        self.verticalLayout_5.addWidget(self.renameAll)

        self.fuseWith = QPushButton(self.categoryGroup)
        self.fuseWith.setObjectName(u"fuseWith")
        sizePolicy2.setHeightForWidth(self.fuseWith.sizePolicy().hasHeightForWidth())
        self.fuseWith.setSizePolicy(sizePolicy2)
        self.fuseWith.setFont(font)
        self.fuseWith.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"border: none;\n"
"border-radius: 15%;padding: 5%;")

        self.verticalLayout_5.addWidget(self.fuseWith)

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


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

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
        self.loadSpinner.setGeometry(QRect(700, 260, 150, 25))
        self.loadSpinner.setMinimumSize(QSize(0, 0))
        self.loadSpinner.setMaximumSize(QSize(150, 25))
        self.horizontalLayout = QHBoxLayout(self.loadSpinner)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.loader = QLabel(self.loadSpinner)
        self.loader.setObjectName(u"loader")
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

        self.verticalLayout.addWidget(self.Awidget)


        self.retranslateUi(home)
        self.createNewFolderFollow.clicked.connect(self.createNewFolder.animateClick)

        QMetaObject.connectSlotsByName(home)
    # setupUi

    def retranslateUi(self, home):
        home.setWindowTitle(QCoreApplication.translate("home", u"Template", None))
        self.category.setText(QCoreApplication.translate("home", u"Cat\u00e9gorie x", None))
        self.renameAll_2.setText(QCoreApplication.translate("home", u"Rafra\u00eechir", None))
        self.renameAll.setText(QCoreApplication.translate("home", u"Tout renommer", None))
        self.fuseWith.setText(QCoreApplication.translate("home", u"Fusionner avec", None))
        self.createNewFolder.setText(QCoreApplication.translate("home", u"Cr\u00e9er un", None))
        self.createNewFolderFollow.setText(QCoreApplication.translate("home", u"   nouveau dossier", None))
        self.oddOldName.setText(QCoreApplication.translate("home", u"<html><head/><body><p>Ancien nom </p></body></html>", None))
        self.oddNewName.setText(QCoreApplication.translate("home", u"Nouveau nom", None))
        self.evenOldName.setText(QCoreApplication.translate("home", u"<html><head/><body><p>Ancien nom</p></body></html>", None))
        self.evenNewName.setText(QCoreApplication.translate("home", u"Nouveau nom", None))
        self.loader.setText("")
        self.operating.setText(QCoreApplication.translate("home", u"Operating ...", None))
    # retranslateUi

