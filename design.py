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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QSizePolicy, QVBoxLayout, QWidget)

from entryandstats import (LabelEdit, LabelStat)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 651)
        MainWindow.setStyleSheet(u"background: #1C1B1F;\n"
"font-family: Product Sans;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(40)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_entry = LabelEdit(self.centralwidget)
        self.lbl_entry.setObjectName(u"lbl_entry")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_entry.sizePolicy().hasHeightForWidth())
        self.lbl_entry.setSizePolicy(sizePolicy)
        self.lbl_entry.setStyleSheet(u"border:none;\n"
"background: transparent;\n"
"font-size: 20pt;\n"
"color:  #5D576B;\n"
"font-weight: 400;")

        self.verticalLayout_2.addWidget(self.lbl_entry)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(14)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_wpm = LabelStat(self.centralwidget)
        self.lbl_wpm.setObjectName(u"lbl_wpm")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_wpm.sizePolicy().hasHeightForWidth())
        self.lbl_wpm.setSizePolicy(sizePolicy1)
        self.lbl_wpm.setMaximumSize(QSize(16777215, 40))
        self.lbl_wpm.setStyleSheet(u"font-family: Product Sans;\n"
"font-size: 14px;\n"
"background:  #D0BCFF;\n"
"color: #381E72;\n"
"min-height: 40px;\n"
"border-radius:  15px;\n"
"padding: 0 14px;\n"
"font-weight: 500;")
        self.lbl_wpm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_wpm)

        self.lbl_accuracy = QLabel(self.centralwidget)
        self.lbl_accuracy.setObjectName(u"lbl_accuracy")
        sizePolicy1.setHeightForWidth(self.lbl_accuracy.sizePolicy().hasHeightForWidth())
        self.lbl_accuracy.setSizePolicy(sizePolicy1)
        self.lbl_accuracy.setMaximumSize(QSize(16777215, 40))
        self.lbl_accuracy.setStyleSheet(u"font-family: Product Sans;\n"
"font-weight: 500;\n"
"font-size: 14px;\n"
"background:  #D0BCFF;\n"
"color: #381E72;\n"
"min-height: 40px;\n"
"border-radius:  15px;\n"
"padding: 0 14px;")
        self.lbl_accuracy.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_accuracy)

        self.lbl_spacer_2 = QLabel(self.centralwidget)
        self.lbl_spacer_2.setObjectName(u"lbl_spacer_2")
        sizePolicy.setHeightForWidth(self.lbl_spacer_2.sizePolicy().hasHeightForWidth())
        self.lbl_spacer_2.setSizePolicy(sizePolicy)
        self.lbl_spacer_2.setStyleSheet(u"color: #666;\n"
"font-size: 16pt;")

        self.horizontalLayout.addWidget(self.lbl_spacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_entry.setText("")
        self.lbl_wpm.setText(QCoreApplication.translate("MainWindow", u"WPM 30", None))
        self.lbl_accuracy.setText(QCoreApplication.translate("MainWindow", u"Accuracy 95%", None))
        self.lbl_spacer_2.setText("")
    # retranslateUi

