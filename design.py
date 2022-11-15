# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background: #222;\n"
"font-family: JetBrainsMono Nerd Font;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_temp = QLabel(self.centralwidget)
        self.lbl_temp.setObjectName(u"lbl_temp")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.lbl_temp)

        self.ln_entry = QLineEdit(self.centralwidget)
        self.ln_entry.setObjectName(u"ln_entry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ln_entry.sizePolicy().hasHeightForWidth())
        self.ln_entry.setSizePolicy(sizePolicy1)
        self.ln_entry.setStyleSheet(u"border:none;\n"
"background: transparent;\n"
"font-size: 20pt;\n"
"color: #fff;\n"
"font-weight: 400;")
        self.ln_entry.setFrame(True)

        self.verticalLayout.addWidget(self.ln_entry)

        self.lbl_wpm = QLabel(self.centralwidget)
        self.lbl_wpm.setObjectName(u"lbl_wpm")
        sizePolicy.setHeightForWidth(self.lbl_wpm.sizePolicy().hasHeightForWidth())
        self.lbl_wpm.setSizePolicy(sizePolicy)
        self.lbl_wpm.setStyleSheet(u"color: #666;\n"
"font-size: 16pt;")

        self.verticalLayout.addWidget(self.lbl_wpm)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_temp.setText("")
        self.ln_entry.setText("")
        self.lbl_wpm.setText("")
    # retranslateUi

