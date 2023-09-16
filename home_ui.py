# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icon_rc

class Ui_Autorenamer(object):
    def setupUi(self, Autorenamer):
        if not Autorenamer.objectName():
            Autorenamer.setObjectName(u"Autorenamer")
        Autorenamer.resize(643, 535)
        Autorenamer.setMinimumSize(QSize(643, 535))
        icon = QIcon()
        icon.addFile(u":/icon/images/icon_2 - Copie - Copie.png", QSize(), QIcon.Normal, QIcon.Off)
        Autorenamer.setWindowIcon(icon)
        self.actionParcourir = QAction(Autorenamer)
        self.actionParcourir.setObjectName(u"actionParcourir")
        self.actionRenommer_tout = QAction(Autorenamer)
        self.actionRenommer_tout.setObjectName(u"actionRenommer_tout")
        self.actionRafra_chir = QAction(Autorenamer)
        self.actionRafra_chir.setObjectName(u"actionRafra_chir")
        self.actionTout_Rafra_chir = QAction(Autorenamer)
        self.actionTout_Rafra_chir.setObjectName(u"actionTout_Rafra_chir")
        self.actionRenommer = QAction(Autorenamer)
        self.actionRenommer.setObjectName(u"actionRenommer")
        self.actionTout_Renommer = QAction(Autorenamer)
        self.actionTout_Renommer.setObjectName(u"actionTout_Renommer")
        self.actionQuitter = QAction(Autorenamer)
        self.actionQuitter.setObjectName(u"actionQuitter")
        self.actionUndo = QAction(Autorenamer)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(Autorenamer)
        self.actionRedo.setObjectName(u"actionRedo")
        self.centralwidget = QWidget(Autorenamer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.firstPart = QWidget(self.centralwidget)
        self.firstPart.setObjectName(u"firstPart")
        self.firstPart.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QVBoxLayout(self.firstPart)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.folderName = QLabel(self.firstPart)
        self.folderName.setObjectName(u"folderName")
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(16)
        self.folderName.setFont(font)
        self.folderName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.folderName)

        self.endFirstPart = QWidget(self.firstPart)
        self.endFirstPart.setObjectName(u"endFirstPart")
        self.verticalLayout_3 = QVBoxLayout(self.endFirstPart)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(105, 0, 105, 0)
        self.folderNameEdit = QLineEdit(self.endFirstPart)
        self.folderNameEdit.setObjectName(u"folderNameEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folderNameEdit.sizePolicy().hasHeightForWidth())
        self.folderNameEdit.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        self.folderNameEdit.setFont(font1)
        self.folderNameEdit.setStyleSheet(u"border: none;\n"
"background-color: rgb(217, 217, 217);\n"
"border-top-left-radius: 15%;\n"
"border-bottom-left-radius: 15%;\n"
"padding-left: 10%;")

        self.horizontalLayout.addWidget(self.folderNameEdit)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.parcourirButton = QPushButton(self.endFirstPart)
        self.parcourirButton.setObjectName(u"parcourirButton")
        sizePolicy.setHeightForWidth(self.parcourirButton.sizePolicy().hasHeightForWidth())
        self.parcourirButton.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(16)
        self.parcourirButton.setFont(font2)
        self.parcourirButton.setLayoutDirection(Qt.RightToLeft)
        self.parcourirButton.setStyleSheet(u"border: none;\n"
"background-color: rgb(241, 241, 241);\n"
"/*border-top-right-radius: 17%;\n"
"border-bottom-right-radius: 17%;*/\n"
"padding-right: 10%;")

        self.horizontalLayout_3.addWidget(self.parcourirButton)

        self.parcourirButton2 = QPushButton(self.endFirstPart)
        self.parcourirButton2.setObjectName(u"parcourirButton2")
        sizePolicy.setHeightForWidth(self.parcourirButton2.sizePolicy().hasHeightForWidth())
        self.parcourirButton2.setSizePolicy(sizePolicy)
        self.parcourirButton2.setFont(font2)
        self.parcourirButton2.setLayoutDirection(Qt.RightToLeft)
        self.parcourirButton2.setStyleSheet(u"border: none;\n"
"background-color: rgb(241, 241, 241);\n"
"border-top-right-radius: 15%;\n"
"border-bottom-right-radius: 15%;")

        self.horizontalLayout_3.addWidget(self.parcourirButton2)

        self.horizontalLayout_3.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.renameAllCategoriesButton = QPushButton(self.endFirstPart)
        self.renameAllCategoriesButton.setObjectName(u"renameAllCategoriesButton")
        sizePolicy.setHeightForWidth(self.renameAllCategoriesButton.sizePolicy().hasHeightForWidth())
        self.renameAllCategoriesButton.setSizePolicy(sizePolicy)
        self.renameAllCategoriesButton.setFont(font2)
        self.renameAllCategoriesButton.setStyleSheet(u"border-radius: 17%;\n"
"background-color: rgb(241, 241, 241);\n"
"margin-left: 125%;\n"
"margin-right: 125%;\n"
"margin-top: 15%;\n"
"margin-bottom: 15%;\n"
"")

        self.horizontalLayout_2.addWidget(self.renameAllCategoriesButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 2)

        self.verticalLayout_2.addWidget(self.endFirstPart)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)

        self.verticalLayout.addWidget(self.firstPart)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border: none;")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 643, 329))
        self.scrollLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollLayout.setObjectName(u"scrollLayout")
        self.emptySearch = QWidget(self.scrollAreaWidgetContents)
        self.emptySearch.setObjectName(u"emptySearch")
        self.emptySearch.setStyleSheet(u"border: 2px dashed; border-radius: 10%;\n"
"border-color: rgb(217, 217, 217);")
        self.verticalLayout_4 = QVBoxLayout(self.emptySearch)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.noFileFound = QLabel(self.emptySearch)
        self.noFileFound.setObjectName(u"noFileFound")
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(16)
        font3.setItalic(True)
        self.noFileFound.setFont(font3)
        self.noFileFound.setStyleSheet(u"border: none;\n"
"color: rgb(217, 217, 217);font-style: italic;")
        self.noFileFound.setAlignment(Qt.AlignCenter)
        self.noFileFound.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.noFileFound)


        self.scrollLayout.addWidget(self.emptySearch)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        Autorenamer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Autorenamer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 643, 21))
        self.menuFichier = QMenu(self.menubar)
        self.menuFichier.setObjectName(u"menuFichier")
        self.menuRenommer = QMenu(self.menubar)
        self.menuRenommer.setObjectName(u"menuRenommer")
        Autorenamer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Autorenamer)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(True)
        Autorenamer.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuRenommer.menuAction())
        self.menuFichier.addAction(self.actionParcourir)
        self.menuFichier.addAction(self.actionQuitter)
        self.menuRenommer.addAction(self.actionUndo)
        self.menuRenommer.addAction(self.actionRedo)
        self.menuRenommer.addSeparator()
        self.menuRenommer.addAction(self.actionTout_Renommer)

        self.retranslateUi(Autorenamer)
        self.parcourirButton2.pressed.connect(self.parcourirButton.animateClick)

        QMetaObject.connectSlotsByName(Autorenamer)
    # setupUi

    def retranslateUi(self, Autorenamer):
        Autorenamer.setWindowTitle(QCoreApplication.translate("Autorenamer", u"Auto Renamer", None))
        self.actionParcourir.setText(QCoreApplication.translate("Autorenamer", u"Parcourir", None))
        self.actionRenommer_tout.setText(QCoreApplication.translate("Autorenamer", u"Renommer tout", None))
        self.actionRafra_chir.setText(QCoreApplication.translate("Autorenamer", u"Rafra\u00eechir", None))
        self.actionTout_Rafra_chir.setText(QCoreApplication.translate("Autorenamer", u"Tout Rafra\u00eechir", None))
        self.actionRenommer.setText(QCoreApplication.translate("Autorenamer", u"Renommer", None))
        self.actionTout_Renommer.setText(QCoreApplication.translate("Autorenamer", u"Tout Renommer", None))
        self.actionQuitter.setText(QCoreApplication.translate("Autorenamer", u"Quitter", None))
        self.actionUndo.setText(QCoreApplication.translate("Autorenamer", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("Autorenamer", u"Redo", None))
        self.folderName.setText(QCoreApplication.translate("Autorenamer", u"Nom du dossier", None))
        self.parcourirButton.setText(QCoreApplication.translate("Autorenamer", u"Parcourir", None))
        self.parcourirButton2.setText("")
        self.renameAllCategoriesButton.setText(QCoreApplication.translate("Autorenamer", u"Renommer toutes les cat\u00e9gories", None))
        self.noFileFound.setText(QCoreApplication.translate("Autorenamer", u"Aucune cat\u00e9gorie trouv\u00e9e ...", None))
        self.menuFichier.setTitle(QCoreApplication.translate("Autorenamer", u"Fichier", None))
        self.menuRenommer.setTitle(QCoreApplication.translate("Autorenamer", u"Edition", None))
    # retranslateUi

