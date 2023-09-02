# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'renamer - Copie.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icon_rc

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
        self.header = QWidget(home)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(660, 72))
        self.header.setStyleSheet(u"background-color: rgb(217, 217, 217);\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.pushButton = QPushButton(self.header)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(62, 62))
        self.pushButton.setMaximumSize(QSize(90, 100))
        self.pushButton.setStyleSheet(u"border-image: url(:/icon/images/icon_2 - Copie.png);\n"
"margin-bottom: 5px;\n"
"margin-top: 5px;")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.horizontalSpacer_3 = QSpacerItem(225, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title = QPushButton(self.header)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(22)
        self.title.setFont(font)
        self.title.setStyleSheet(u"border: none;\n"
"padding-left: -160%;")

        self.horizontalLayout.addWidget(self.title)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 3)
        self.horizontalLayout_3.setStretch(3, 12)

        self.verticalLayout.addWidget(self.header)

        self.Awidget = QWidget(home)
        self.Awidget.setObjectName(u"Awidget")
        self.Awidget.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 242, 175);")
        self.categoryGroup = QWidget(self.Awidget)
        self.categoryGroup.setObjectName(u"categoryGroup")
        self.categoryGroup.setGeometry(QRect(30, 30, 531, 331))
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
        font1 = QFont()
        font1.setPointSize(16)
        self.category.setFont(font1)
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
        self.renameAll = QPushButton(self.categoryGroup)
        self.renameAll.setObjectName(u"renameAll")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.renameAll.sizePolicy().hasHeightForWidth())
        self.renameAll.setSizePolicy(sizePolicy2)
        self.renameAll.setFont(font1)
        self.renameAll.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"border: none;\n"
"border-radius: 15%;padding: 5%;")

        self.verticalLayout_5.addWidget(self.renameAll)

        self.fuseWith = QPushButton(self.categoryGroup)
        self.fuseWith.setObjectName(u"fuseWith")
        sizePolicy2.setHeightForWidth(self.fuseWith.sizePolicy().hasHeightForWidth())
        self.fuseWith.setSizePolicy(sizePolicy2)
        self.fuseWith.setFont(font1)
        self.fuseWith.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"border: none;\n"
"border-radius: 15%;padding: 5%;")

        self.verticalLayout_5.addWidget(self.fuseWith)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.createNewFolder = QCheckBox(self.categoryGroup)
        self.createNewFolder.setObjectName(u"createNewFolder")
        self.createNewFolder.setFont(font1)

        self.verticalLayout_4.addWidget(self.createNewFolder)

        self.createNewFolderFollow = QPushButton(self.categoryGroup)
        self.createNewFolderFollow.setObjectName(u"createNewFolderFollow")
        self.createNewFolderFollow.setFont(font1)
        self.createNewFolderFollow.setStyleSheet(u"border: none;")

        self.verticalLayout_4.addWidget(self.createNewFolderFollow)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.categoryGroup_2 = QWidget(self.Awidget)
        self.categoryGroup_2.setObjectName(u"categoryGroup_2")
        self.categoryGroup_2.setGeometry(QRect(30, 380, 531, 331))
        self.categoryGroup_2.setMinimumSize(QSize(0, 0))
        self.categoryGroup_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout_6 = QHBoxLayout(self.categoryGroup_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.categoryEntity_2 = QWidget(self.categoryGroup_2)
        self.categoryEntity_2.setObjectName(u"categoryEntity_2")
        self.categoryEntity_2.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.categoryEntity_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.categoryContainer_2 = QWidget(self.categoryEntity_2)
        self.categoryContainer_2.setObjectName(u"categoryContainer_2")
        self.categoryContainer_2.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.categoryContainer_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.category_2 = QLineEdit(self.categoryContainer_2)
        self.category_2.setObjectName(u"category_2")
        sizePolicy1.setHeightForWidth(self.category_2.sizePolicy().hasHeightForWidth())
        self.category_2.setSizePolicy(sizePolicy1)
        self.category_2.setMinimumSize(QSize(0, 0))
        self.category_2.setFont(font1)
        self.category_2.setStyleSheet(u"background-color: rgb(217, 217, 217);\n"
"border: none;\n"
"border-top-right-radius: 16%;\n"
"border-top-left-radius: 16%;")
        self.category_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.category_2)


        self.verticalLayout_6.addWidget(self.categoryContainer_2)

        self.evenContainer_2 = QWidget(self.categoryEntity_2)
        self.evenContainer_2.setObjectName(u"evenContainer_2")
        self.evenContainer_2.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.horizontalLayout_7 = QHBoxLayout(self.evenContainer_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.oldName_2 = QLabel(self.evenContainer_2)
        self.oldName_2.setObjectName(u"oldName_2")
        font2 = QFont()
        font2.setPointSize(14)
        self.oldName_2.setFont(font2)
        self.oldName_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.oldName_2)

        self.newName_2 = QLineEdit(self.evenContainer_2)
        self.newName_2.setObjectName(u"newName_2")
        self.newName_2.setFont(font2)
        self.newName_2.setStyleSheet(u"border: none;\n"
"background: transparent;")

        self.horizontalLayout_7.addWidget(self.newName_2)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)

        self.verticalLayout_6.addWidget(self.evenContainer_2)

        self.oddContainer_2 = QWidget(self.categoryEntity_2)
        self.oddContainer_2.setObjectName(u"oddContainer_2")
        self.oddContainer_2.setStyleSheet(u"border: none;")
        self.horizontalLayout_8 = QHBoxLayout(self.oddContainer_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.oldName2_2 = QLabel(self.oddContainer_2)
        self.oldName2_2.setObjectName(u"oldName2_2")
        self.oldName2_2.setFont(font2)
        self.oldName2_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.oldName2_2)

        self.newName2_2 = QLineEdit(self.oddContainer_2)
        self.newName2_2.setObjectName(u"newName2_2")
        self.newName2_2.setFont(font2)
        self.newName2_2.setStyleSheet(u"border: none;\n"
"background: transparent;")

        self.horizontalLayout_8.addWidget(self.newName2_2)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)

        self.verticalLayout_6.addWidget(self.oddContainer_2)


        self.horizontalLayout_6.addWidget(self.categoryEntity_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.renameAll_2 = QPushButton(self.categoryGroup_2)
        self.renameAll_2.setObjectName(u"renameAll_2")
        sizePolicy2.setHeightForWidth(self.renameAll_2.sizePolicy().hasHeightForWidth())
        self.renameAll_2.setSizePolicy(sizePolicy2)
        self.renameAll_2.setFont(font1)
        self.renameAll_2.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"border: none;\n"
"border-radius: 15%;padding: 5%;")

        self.verticalLayout_8.addWidget(self.renameAll_2)

        self.fuseWith_2 = QPushButton(self.categoryGroup_2)
        self.fuseWith_2.setObjectName(u"fuseWith_2")
        sizePolicy2.setHeightForWidth(self.fuseWith_2.sizePolicy().hasHeightForWidth())
        self.fuseWith_2.setSizePolicy(sizePolicy2)
        self.fuseWith_2.setFont(font1)
        self.fuseWith_2.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"border: none;\n"
"border-radius: 15%;padding: 5%;")

        self.verticalLayout_8.addWidget(self.fuseWith_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.createNewFolder_2 = QCheckBox(self.categoryGroup_2)
        self.createNewFolder_2.setObjectName(u"createNewFolder_2")
        self.createNewFolder_2.setFont(font1)

        self.verticalLayout_9.addWidget(self.createNewFolder_2)

        self.createNewFolderFollow_2 = QPushButton(self.categoryGroup_2)
        self.createNewFolderFollow_2.setObjectName(u"createNewFolderFollow_2")
        self.createNewFolderFollow_2.setFont(font1)
        self.createNewFolderFollow_2.setStyleSheet(u"border: none;")

        self.verticalLayout_9.addWidget(self.createNewFolderFollow_2)


        self.verticalLayout_8.addLayout(self.verticalLayout_9)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addLayout(self.verticalLayout_8)

        self.oddContainer = QWidget(self.Awidget)
        self.oddContainer.setObjectName(u"oddContainer")
        self.oddContainer.setGeometry(QRect(590, 90, 281, 50))
        self.oddContainer.setMinimumSize(QSize(0, 50))
        self.oddContainer.setStyleSheet(u"border: none;")
        self.horizontalLayout_4 = QHBoxLayout(self.oddContainer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.oddOldName = QLabel(self.oddContainer)
        self.oddOldName.setObjectName(u"oddOldName")
        self.oddOldName.setFont(font2)
        self.oddOldName.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.oddOldName)

        self.oddNewName = QLineEdit(self.oddContainer)
        self.oddNewName.setObjectName(u"oddNewName")
        self.oddNewName.setFont(font2)
        self.oddNewName.setStyleSheet(u"border: none;\n"
"background: transparent;")

        self.horizontalLayout_4.addWidget(self.oddNewName)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.evenContainer = QWidget(self.Awidget)
        self.evenContainer.setObjectName(u"evenContainer")
        self.evenContainer.setGeometry(QRect(650, 185, 211, 51))
        self.evenContainer.setMinimumSize(QSize(0, 50))
        self.evenContainer.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.horizontalLayout_2 = QHBoxLayout(self.evenContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.evenOldName = QLabel(self.evenContainer)
        self.evenOldName.setObjectName(u"evenOldName")
        self.evenOldName.setFont(font2)
        self.evenOldName.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.evenOldName)

        self.evenNewName = QLineEdit(self.evenContainer)
        self.evenNewName.setObjectName(u"evenNewName")
        self.evenNewName.setFont(font2)
        self.evenNewName.setStyleSheet(u"border: none;\n"
"background: transparent;")

        self.horizontalLayout_2.addWidget(self.evenNewName)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addWidget(self.Awidget)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 6)

        self.retranslateUi(home)
        self.createNewFolderFollow.clicked.connect(self.createNewFolder.animateClick)

        QMetaObject.connectSlotsByName(home)
    # setupUi

    def retranslateUi(self, home):
        home.setWindowTitle(QCoreApplication.translate("home", u"Template", None))
        self.pushButton.setText("")
        self.title.setText(QCoreApplication.translate("home", u"Auto renamer", None))
        self.category.setText(QCoreApplication.translate("home", u"Cat\u00e9gorie x", None))
        self.renameAll.setText(QCoreApplication.translate("home", u"Tout renommer", None))
        self.fuseWith.setText(QCoreApplication.translate("home", u"Fusionner avec", None))
        self.createNewFolder.setText(QCoreApplication.translate("home", u"Cr\u00e9er un", None))
        self.createNewFolderFollow.setText(QCoreApplication.translate("home", u"   nouveau dossier", None))
        self.category_2.setText(QCoreApplication.translate("home", u"Cat\u00e9gorie x", None))
        self.oldName_2.setText(QCoreApplication.translate("home", u"<html><head/><body><p><span style=\" text-decoration: line-through;\">Ancien nom</span></p></body></html>", None))
        self.newName_2.setText(QCoreApplication.translate("home", u"Nouveau nom", None))
        self.oldName2_2.setText(QCoreApplication.translate("home", u"<html><head/><body><p><span style=\" text-decoration: line-through;\">Ancien nom</span></p></body></html>", None))
        self.newName2_2.setText(QCoreApplication.translate("home", u"Nouveau nom", None))
        self.renameAll_2.setText(QCoreApplication.translate("home", u"Tout renommer", None))
        self.fuseWith_2.setText(QCoreApplication.translate("home", u"Fusionner avec", None))
        self.createNewFolder_2.setText(QCoreApplication.translate("home", u"Cr\u00e9er un", None))
        self.createNewFolderFollow_2.setText(QCoreApplication.translate("home", u"   nouveau dossier", None))
        self.oddOldName.setText(QCoreApplication.translate("home", u"<html><head/><body><p><span style=\" text-decoration: line-through;\">Ancien nom</span></p></body></html>", None))
        self.oddNewName.setText(QCoreApplication.translate("home", u"Nouveau nom", None))
        self.evenOldName.setText(QCoreApplication.translate("home", u"<html><head/><body><p><span style=\" text-decoration: line-through;\">Ancien nom</span></p></body></html>", None))
        self.evenNewName.setText(QCoreApplication.translate("home", u"Nouveau nom", None))
    # retranslateUi

