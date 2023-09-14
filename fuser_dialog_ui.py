# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fuser_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icon_rc

class Ui_fuser(object):
    def setupUi(self, fuser):
        if not fuser.objectName():
            fuser.setObjectName(u"fuser")
        fuser.resize(487, 301)
        fuser.setMinimumSize(QSize(487, 301))
        fuser.setMaximumSize(QSize(487, 301))
        icon = QIcon()
        icon.addFile(u":/icon/images/icon_2 - Copie - Copie.png", QSize(), QIcon.Normal, QIcon.Off)
        fuser.setWindowIcon(icon)
        fuser.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(fuser)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fuserQuestion = QLabel(fuser)
        self.fuserQuestion.setObjectName(u"fuserQuestion")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fuserQuestion.sizePolicy().hasHeightForWidth())
        self.fuserQuestion.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.fuserQuestion.setFont(font)
        self.fuserQuestion.setStyleSheet(u"text-decoration: none;")
        self.fuserQuestion.setAlignment(Qt.AlignCenter)
        self.fuserQuestion.setWordWrap(True)

        self.verticalLayout.addWidget(self.fuserQuestion)

        self.scrollArea = QScrollArea(fuser)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border: none;")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 469, 189))
        self.scrollLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollLayout.setSpacing(60)
        self.scrollLayout.setObjectName(u"scrollLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.okLayout = QHBoxLayout()
        self.okLayout.setObjectName(u"okLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.okLayout.addItem(self.horizontalSpacer)

        self.ok = QPushButton(fuser)
        self.ok.setObjectName(u"ok")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ok.sizePolicy().hasHeightForWidth())
        self.ok.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(16)
        self.ok.setFont(font1)
        self.ok.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"border: 1px solid black;\n"
"border-radius: 0%;padding: 5%;margin: 10% 0%;")

        self.okLayout.addWidget(self.ok)


        self.verticalLayout.addLayout(self.okLayout)


        self.retranslateUi(fuser)

        QMetaObject.connectSlotsByName(fuser)
    # setupUi

    def retranslateUi(self, fuser):
        fuser.setWindowTitle(QCoreApplication.translate("fuser", u"Choisissez la cat\u00e9gorie - Autorenamer", None))
        self.fuserQuestion.setText(QCoreApplication.translate("fuser", u"<html><head/><body><p>Avec quelle cat\u00e9gorie souhaitez-vous la fusionner ?</p></body></html>", None))
        self.ok.setText(QCoreApplication.translate("fuser", u"OK", None))
    # retranslateUi

