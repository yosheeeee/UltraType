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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from entryandstats import (LabelEdit, LabelStat)
from keyboard import Keyboard

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1044, 618)
        MainWindow.setMinimumSize(QSize(936, 0))
        MainWindow.setStyleSheet(u"QWidget {\n"
"	background: #1C1B1F;\n"
"	font-family: Product Sans;\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: #E8DEF8;\n"
"	font-size: 15px;\n"
"	background-color:  #302D38;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #4A4458;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #68627A;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setStyleSheet(u"padding ")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.verticalWidget = QWidget(self.centralwidget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setMinimumSize(QSize(936, 0))
        self.verticalWidget.setMaximumSize(QSize(936, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 40, 0, 40)
        self.lt_stats_and_entry = QVBoxLayout()
        self.lt_stats_and_entry.setSpacing(0)
        self.lt_stats_and_entry.setObjectName(u"lt_stats_and_entry")
        self.lt_stats_and_entry.setContentsMargins(-1, -1, -1, 0)
        self.lbl_entry = LabelEdit(self.verticalWidget)
        self.lbl_entry.setObjectName(u"lbl_entry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_entry.sizePolicy().hasHeightForWidth())
        self.lbl_entry.setSizePolicy(sizePolicy1)
        self.lbl_entry.setStyleSheet(u"border:none;\n"
"background: transparent;\n"
"font-size: 20pt;\n"
"color:  #5D576B;\n"
"font-weight: 400;\n"
"font-family: Roboto Mono;")
        self.lbl_entry.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl_entry.setWordWrap(True)

        self.lt_stats_and_entry.addWidget(self.lbl_entry)

        self.lt_stats = QHBoxLayout()
        self.lt_stats.setSpacing(14)
        self.lt_stats.setObjectName(u"lt_stats")
        self.lt_stats.setContentsMargins(-1, 20, -1, 20)
        self.lbl_wpm = LabelStat(self.verticalWidget)
        self.lbl_wpm.setObjectName(u"lbl_wpm")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbl_wpm.sizePolicy().hasHeightForWidth())
        self.lbl_wpm.setSizePolicy(sizePolicy2)
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

        self.lt_stats.addWidget(self.lbl_wpm)

        self.lbl_accuracy = LabelStat(self.verticalWidget)
        self.lbl_accuracy.setObjectName(u"lbl_accuracy")
        sizePolicy2.setHeightForWidth(self.lbl_accuracy.sizePolicy().hasHeightForWidth())
        self.lbl_accuracy.setSizePolicy(sizePolicy2)
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

        self.lt_stats.addWidget(self.lbl_accuracy)

        self.lbl_spacer_2 = QLabel(self.verticalWidget)
        self.lbl_spacer_2.setObjectName(u"lbl_spacer_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbl_spacer_2.sizePolicy().hasHeightForWidth())
        self.lbl_spacer_2.setSizePolicy(sizePolicy3)
        self.lbl_spacer_2.setStyleSheet(u"color: #666;\n"
"font-size: 16pt;")

        self.lt_stats.addWidget(self.lbl_spacer_2)


        self.lt_stats_and_entry.addLayout(self.lt_stats)


        self.verticalLayout_8.addLayout(self.lt_stats_and_entry)

        self.wt_keyboard = Keyboard(self.verticalWidget)
        self.wt_keyboard.setObjectName(u"wt_keyboard")
        self.wt_keyboard.setEnabled(True)
        self.lt_keyboard = QVBoxLayout(self.wt_keyboard)
        self.lt_keyboard.setSpacing(9)
        self.lt_keyboard.setObjectName(u"lt_keyboard")
        self.lt_keyboard.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_14 = QPushButton(self.wt_keyboard)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy4)
        self.pushButton_14.setMinimumSize(QSize(55, 55))
        self.pushButton_14.setMaximumSize(QSize(55, 55))
        self.pushButton_14.setBaseSize(QSize(40, 40))
        self.pushButton_14.setTabletTracking(False)
        self.pushButton_14.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.pushButton_14)

        self.pushButton_13 = QPushButton(self.wt_keyboard)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy4.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy4)
        self.pushButton_13.setMinimumSize(QSize(55, 55))
        self.pushButton_13.setMaximumSize(QSize(55, 55))
        self.pushButton_13.setBaseSize(QSize(40, 40))
        self.pushButton_13.setTabletTracking(False)
        self.pushButton_13.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.pushButton_13)

        self.pushButton_12 = QPushButton(self.wt_keyboard)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy4.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy4)
        self.pushButton_12.setMinimumSize(QSize(55, 55))
        self.pushButton_12.setMaximumSize(QSize(55, 55))
        self.pushButton_12.setBaseSize(QSize(40, 40))
        self.pushButton_12.setTabletTracking(False)
        self.pushButton_12.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.pushButton_12)

        self.pushButton_11 = QPushButton(self.wt_keyboard)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy4.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy4)
        self.pushButton_11.setMinimumSize(QSize(55, 55))
        self.pushButton_11.setMaximumSize(QSize(55, 55))
        self.pushButton_11.setBaseSize(QSize(40, 40))
        self.pushButton_11.setTabletTracking(False)
        self.pushButton_11.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.pushButton_11)

        self.pushButton_10 = QPushButton(self.wt_keyboard)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy4.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy4)
        self.pushButton_10.setMinimumSize(QSize(55, 55))
        self.pushButton_10.setMaximumSize(QSize(55, 55))
        self.pushButton_10.setBaseSize(QSize(40, 40))
        self.pushButton_10.setTabletTracking(False)
        self.pushButton_10.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.pushButton_10)

        self.pushButton_9 = QPushButton(self.wt_keyboard)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy4.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy4)
        self.pushButton_9.setMinimumSize(QSize(55, 55))
        self.pushButton_9.setMaximumSize(QSize(55, 55))
        self.pushButton_9.setBaseSize(QSize(40, 40))
        self.pushButton_9.setTabletTracking(False)
        self.pushButton_9.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.wt_keyboard)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy4.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy4)
        self.pushButton_8.setMinimumSize(QSize(55, 55))
        self.pushButton_8.setMaximumSize(QSize(55, 55))
        self.pushButton_8.setBaseSize(QSize(40, 40))
        self.pushButton_8.setTabletTracking(False)
        self.pushButton_8.setFocusPolicy(Qt.NoFocus)
        self.pushButton_8.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.wt_keyboard)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy4.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy4)
        self.pushButton_7.setMinimumSize(QSize(55, 55))
        self.pushButton_7.setMaximumSize(QSize(55, 55))
        self.pushButton_7.setBaseSize(QSize(40, 40))
        self.pushButton_7.setTabletTracking(False)
        self.pushButton_7.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.wt_keyboard)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy4.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy4)
        self.pushButton_6.setMinimumSize(QSize(55, 55))
        self.pushButton_6.setMaximumSize(QSize(55, 55))
        self.pushButton_6.setBaseSize(QSize(40, 40))
        self.pushButton_6.setTabletTracking(False)
        self.pushButton_6.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.wt_keyboard)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy4.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy4)
        self.pushButton_5.setMinimumSize(QSize(55, 55))
        self.pushButton_5.setMaximumSize(QSize(55, 55))
        self.pushButton_5.setBaseSize(QSize(40, 40))
        self.pushButton_5.setTabletTracking(False)
        self.pushButton_5.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.pushButton_5)

        self.pushButton_52 = QPushButton(self.wt_keyboard)
        self.pushButton_52.setObjectName(u"pushButton_52")
        sizePolicy4.setHeightForWidth(self.pushButton_52.sizePolicy().hasHeightForWidth())
        self.pushButton_52.setSizePolicy(sizePolicy4)
        self.pushButton_52.setMinimumSize(QSize(55, 55))
        self.pushButton_52.setMaximumSize(QSize(55, 55))
        self.pushButton_52.setBaseSize(QSize(40, 40))
        self.pushButton_52.setTabletTracking(False)
        self.pushButton_52.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.pushButton_52)

        self.pushButton_51 = QPushButton(self.wt_keyboard)
        self.pushButton_51.setObjectName(u"pushButton_51")
        sizePolicy4.setHeightForWidth(self.pushButton_51.sizePolicy().hasHeightForWidth())
        self.pushButton_51.setSizePolicy(sizePolicy4)
        self.pushButton_51.setMinimumSize(QSize(55, 55))
        self.pushButton_51.setMaximumSize(QSize(55, 55))
        self.pushButton_51.setBaseSize(QSize(40, 40))
        self.pushButton_51.setTabletTracking(False)
        self.pushButton_51.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.pushButton_51)

        self.pushButton_4 = QPushButton(self.wt_keyboard)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy4.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy4)
        self.pushButton_4.setMinimumSize(QSize(55, 55))
        self.pushButton_4.setMaximumSize(QSize(55, 55))
        self.pushButton_4.setBaseSize(QSize(40, 40))
        self.pushButton_4.setTabletTracking(False)
        self.pushButton_4.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.pushButton_4)

        self.btn_backspace = QPushButton(self.wt_keyboard)
        self.btn_backspace.setObjectName(u"btn_backspace")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy5)
        self.btn_backspace.setMinimumSize(QSize(55, 55))
        self.btn_backspace.setMaximumSize(QSize(1000, 55))
        self.btn_backspace.setBaseSize(QSize(40, 40))
        self.btn_backspace.setTabletTracking(False)
        self.btn_backspace.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.btn_backspace)


        self.lt_keyboard.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_tab = QPushButton(self.wt_keyboard)
        self.btn_tab.setObjectName(u"btn_tab")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btn_tab.sizePolicy().hasHeightForWidth())
        self.btn_tab.setSizePolicy(sizePolicy6)
        self.btn_tab.setMinimumSize(QSize(55, 55))
        self.btn_tab.setMaximumSize(QSize(1000, 55))
        self.btn_tab.setBaseSize(QSize(40, 40))
        self.btn_tab.setFocusPolicy(Qt.NoFocus)
        self.btn_tab.setCheckable(False)
        self.btn_tab.setAutoDefault(False)

        self.horizontalLayout_12.addWidget(self.btn_tab)

        self.btn_1 = QPushButton(self.wt_keyboard)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy4.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy4)
        self.btn_1.setMinimumSize(QSize(55, 55))
        self.btn_1.setMaximumSize(QSize(55, 55))
        self.btn_1.setBaseSize(QSize(40, 40))
        self.btn_1.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_1)

        self.btn_2 = QPushButton(self.wt_keyboard)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy4.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy4)
        self.btn_2.setMinimumSize(QSize(55, 55))
        self.btn_2.setMaximumSize(QSize(55, 55))
        self.btn_2.setBaseSize(QSize(40, 40))
        self.btn_2.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_2)

        self.btn_3 = QPushButton(self.wt_keyboard)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy4.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy4)
        self.btn_3.setMinimumSize(QSize(55, 55))
        self.btn_3.setMaximumSize(QSize(55, 55))
        self.btn_3.setBaseSize(QSize(40, 40))
        self.btn_3.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_3)

        self.btn_4 = QPushButton(self.wt_keyboard)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy4.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy4)
        self.btn_4.setMinimumSize(QSize(55, 55))
        self.btn_4.setMaximumSize(QSize(55, 55))
        self.btn_4.setBaseSize(QSize(40, 40))
        self.btn_4.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_4)

        self.btn_5 = QPushButton(self.wt_keyboard)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy4.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy4)
        self.btn_5.setMinimumSize(QSize(55, 55))
        self.btn_5.setMaximumSize(QSize(55, 55))
        self.btn_5.setBaseSize(QSize(40, 40))
        self.btn_5.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_5)

        self.btn_6 = QPushButton(self.wt_keyboard)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy4.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy4)
        self.btn_6.setMinimumSize(QSize(55, 55))
        self.btn_6.setMaximumSize(QSize(55, 55))
        self.btn_6.setBaseSize(QSize(40, 40))
        self.btn_6.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_6)

        self.btn_7 = QPushButton(self.wt_keyboard)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy4.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy4)
        self.btn_7.setMinimumSize(QSize(55, 55))
        self.btn_7.setMaximumSize(QSize(55, 55))
        self.btn_7.setBaseSize(QSize(40, 40))
        self.btn_7.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_7)

        self.btn_8 = QPushButton(self.wt_keyboard)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy4.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy4)
        self.btn_8.setMinimumSize(QSize(55, 55))
        self.btn_8.setMaximumSize(QSize(55, 55))
        self.btn_8.setBaseSize(QSize(40, 40))
        self.btn_8.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_8)

        self.btn_9 = QPushButton(self.wt_keyboard)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy4.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy4)
        self.btn_9.setMinimumSize(QSize(55, 55))
        self.btn_9.setMaximumSize(QSize(55, 55))
        self.btn_9.setBaseSize(QSize(40, 40))
        self.btn_9.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_9)

        self.btn_10 = QPushButton(self.wt_keyboard)
        self.btn_10.setObjectName(u"btn_10")
        sizePolicy4.setHeightForWidth(self.btn_10.sizePolicy().hasHeightForWidth())
        self.btn_10.setSizePolicy(sizePolicy4)
        self.btn_10.setMinimumSize(QSize(55, 55))
        self.btn_10.setMaximumSize(QSize(55, 55))
        self.btn_10.setBaseSize(QSize(40, 40))
        self.btn_10.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_10)

        self.btn_11 = QPushButton(self.wt_keyboard)
        self.btn_11.setObjectName(u"btn_11")
        sizePolicy4.setHeightForWidth(self.btn_11.sizePolicy().hasHeightForWidth())
        self.btn_11.setSizePolicy(sizePolicy4)
        self.btn_11.setMinimumSize(QSize(55, 55))
        self.btn_11.setMaximumSize(QSize(55, 55))
        self.btn_11.setBaseSize(QSize(40, 40))
        self.btn_11.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_11)

        self.btn_12 = QPushButton(self.wt_keyboard)
        self.btn_12.setObjectName(u"btn_12")
        sizePolicy4.setHeightForWidth(self.btn_12.sizePolicy().hasHeightForWidth())
        self.btn_12.setSizePolicy(sizePolicy4)
        self.btn_12.setMinimumSize(QSize(55, 55))
        self.btn_12.setMaximumSize(QSize(55, 55))
        self.btn_12.setBaseSize(QSize(40, 40))
        self.btn_12.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_12)

        self.btn_backslash = QPushButton(self.wt_keyboard)
        self.btn_backslash.setObjectName(u"btn_backslash")
        sizePolicy4.setHeightForWidth(self.btn_backslash.sizePolicy().hasHeightForWidth())
        self.btn_backslash.setSizePolicy(sizePolicy4)
        self.btn_backslash.setMinimumSize(QSize(55, 55))
        self.btn_backslash.setMaximumSize(QSize(55, 55))
        self.btn_backslash.setBaseSize(QSize(40, 40))
        self.btn_backslash.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_backslash)


        self.lt_keyboard.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_caps = QPushButton(self.wt_keyboard)
        self.btn_caps.setObjectName(u"btn_caps")
        sizePolicy6.setHeightForWidth(self.btn_caps.sizePolicy().hasHeightForWidth())
        self.btn_caps.setSizePolicy(sizePolicy6)
        self.btn_caps.setMinimumSize(QSize(55, 55))
        self.btn_caps.setMaximumSize(QSize(1000, 55))
        self.btn_caps.setBaseSize(QSize(40, 40))
        self.btn_caps.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_caps)

        self.btn_13 = QPushButton(self.wt_keyboard)
        self.btn_13.setObjectName(u"btn_13")
        sizePolicy4.setHeightForWidth(self.btn_13.sizePolicy().hasHeightForWidth())
        self.btn_13.setSizePolicy(sizePolicy4)
        self.btn_13.setMinimumSize(QSize(55, 55))
        self.btn_13.setMaximumSize(QSize(55, 55))
        self.btn_13.setBaseSize(QSize(40, 40))
        self.btn_13.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_13)

        self.btn_14 = QPushButton(self.wt_keyboard)
        self.btn_14.setObjectName(u"btn_14")
        sizePolicy4.setHeightForWidth(self.btn_14.sizePolicy().hasHeightForWidth())
        self.btn_14.setSizePolicy(sizePolicy4)
        self.btn_14.setMinimumSize(QSize(55, 55))
        self.btn_14.setMaximumSize(QSize(55, 55))
        self.btn_14.setBaseSize(QSize(40, 40))
        self.btn_14.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_14)

        self.btn_15 = QPushButton(self.wt_keyboard)
        self.btn_15.setObjectName(u"btn_15")
        sizePolicy4.setHeightForWidth(self.btn_15.sizePolicy().hasHeightForWidth())
        self.btn_15.setSizePolicy(sizePolicy4)
        self.btn_15.setMinimumSize(QSize(55, 55))
        self.btn_15.setMaximumSize(QSize(55, 55))
        self.btn_15.setBaseSize(QSize(40, 40))
        self.btn_15.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_15)

        self.btn_16 = QPushButton(self.wt_keyboard)
        self.btn_16.setObjectName(u"btn_16")
        sizePolicy4.setHeightForWidth(self.btn_16.sizePolicy().hasHeightForWidth())
        self.btn_16.setSizePolicy(sizePolicy4)
        self.btn_16.setMinimumSize(QSize(55, 55))
        self.btn_16.setMaximumSize(QSize(55, 55))
        self.btn_16.setBaseSize(QSize(40, 40))
        self.btn_16.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_16)

        self.btn_17 = QPushButton(self.wt_keyboard)
        self.btn_17.setObjectName(u"btn_17")
        sizePolicy4.setHeightForWidth(self.btn_17.sizePolicy().hasHeightForWidth())
        self.btn_17.setSizePolicy(sizePolicy4)
        self.btn_17.setMinimumSize(QSize(55, 55))
        self.btn_17.setMaximumSize(QSize(55, 55))
        self.btn_17.setBaseSize(QSize(40, 40))
        self.btn_17.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_17)

        self.btn_18 = QPushButton(self.wt_keyboard)
        self.btn_18.setObjectName(u"btn_18")
        sizePolicy4.setHeightForWidth(self.btn_18.sizePolicy().hasHeightForWidth())
        self.btn_18.setSizePolicy(sizePolicy4)
        self.btn_18.setMinimumSize(QSize(55, 55))
        self.btn_18.setMaximumSize(QSize(55, 55))
        self.btn_18.setBaseSize(QSize(40, 40))
        self.btn_18.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_18)

        self.btn_19 = QPushButton(self.wt_keyboard)
        self.btn_19.setObjectName(u"btn_19")
        sizePolicy4.setHeightForWidth(self.btn_19.sizePolicy().hasHeightForWidth())
        self.btn_19.setSizePolicy(sizePolicy4)
        self.btn_19.setMinimumSize(QSize(55, 55))
        self.btn_19.setMaximumSize(QSize(55, 55))
        self.btn_19.setBaseSize(QSize(40, 40))
        self.btn_19.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_19)

        self.btn_20 = QPushButton(self.wt_keyboard)
        self.btn_20.setObjectName(u"btn_20")
        sizePolicy4.setHeightForWidth(self.btn_20.sizePolicy().hasHeightForWidth())
        self.btn_20.setSizePolicy(sizePolicy4)
        self.btn_20.setMinimumSize(QSize(55, 55))
        self.btn_20.setMaximumSize(QSize(55, 55))
        self.btn_20.setBaseSize(QSize(40, 40))
        self.btn_20.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_20)

        self.btn_21 = QPushButton(self.wt_keyboard)
        self.btn_21.setObjectName(u"btn_21")
        sizePolicy4.setHeightForWidth(self.btn_21.sizePolicy().hasHeightForWidth())
        self.btn_21.setSizePolicy(sizePolicy4)
        self.btn_21.setMinimumSize(QSize(55, 55))
        self.btn_21.setMaximumSize(QSize(55, 55))
        self.btn_21.setBaseSize(QSize(40, 40))
        self.btn_21.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_21)

        self.btn_22 = QPushButton(self.wt_keyboard)
        self.btn_22.setObjectName(u"btn_22")
        sizePolicy4.setHeightForWidth(self.btn_22.sizePolicy().hasHeightForWidth())
        self.btn_22.setSizePolicy(sizePolicy4)
        self.btn_22.setMinimumSize(QSize(55, 55))
        self.btn_22.setMaximumSize(QSize(55, 55))
        self.btn_22.setBaseSize(QSize(40, 40))
        self.btn_22.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_22)

        self.btn_23 = QPushButton(self.wt_keyboard)
        self.btn_23.setObjectName(u"btn_23")
        sizePolicy4.setHeightForWidth(self.btn_23.sizePolicy().hasHeightForWidth())
        self.btn_23.setSizePolicy(sizePolicy4)
        self.btn_23.setMinimumSize(QSize(55, 55))
        self.btn_23.setMaximumSize(QSize(55, 55))
        self.btn_23.setBaseSize(QSize(40, 40))
        self.btn_23.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_23)

        self.btn_enter = QPushButton(self.wt_keyboard)
        self.btn_enter.setObjectName(u"btn_enter")
        sizePolicy6.setHeightForWidth(self.btn_enter.sizePolicy().hasHeightForWidth())
        self.btn_enter.setSizePolicy(sizePolicy6)
        self.btn_enter.setMinimumSize(QSize(55, 55))
        self.btn_enter.setMaximumSize(QSize(1000, 55))
        self.btn_enter.setBaseSize(QSize(40, 40))
        self.btn_enter.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_enter)


        self.lt_keyboard.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_lshift = QPushButton(self.wt_keyboard)
        self.btn_lshift.setObjectName(u"btn_lshift")
        sizePolicy6.setHeightForWidth(self.btn_lshift.sizePolicy().hasHeightForWidth())
        self.btn_lshift.setSizePolicy(sizePolicy6)
        self.btn_lshift.setMinimumSize(QSize(55, 55))
        self.btn_lshift.setMaximumSize(QSize(1000, 55))
        self.btn_lshift.setBaseSize(QSize(40, 40))
        self.btn_lshift.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.btn_lshift)

        self.btn_24 = QPushButton(self.wt_keyboard)
        self.btn_24.setObjectName(u"btn_24")
        sizePolicy4.setHeightForWidth(self.btn_24.sizePolicy().hasHeightForWidth())
        self.btn_24.setSizePolicy(sizePolicy4)
        self.btn_24.setMinimumSize(QSize(55, 55))
        self.btn_24.setMaximumSize(QSize(55, 55))
        self.btn_24.setBaseSize(QSize(40, 40))
        self.btn_24.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.btn_24)

        self.btn_25 = QPushButton(self.wt_keyboard)
        self.btn_25.setObjectName(u"btn_25")
        sizePolicy4.setHeightForWidth(self.btn_25.sizePolicy().hasHeightForWidth())
        self.btn_25.setSizePolicy(sizePolicy4)
        self.btn_25.setMinimumSize(QSize(55, 55))
        self.btn_25.setMaximumSize(QSize(55, 55))
        self.btn_25.setBaseSize(QSize(40, 40))
        self.btn_25.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.btn_25)

        self.btn_26 = QPushButton(self.wt_keyboard)
        self.btn_26.setObjectName(u"btn_26")
        sizePolicy4.setHeightForWidth(self.btn_26.sizePolicy().hasHeightForWidth())
        self.btn_26.setSizePolicy(sizePolicy4)
        self.btn_26.setMinimumSize(QSize(55, 55))
        self.btn_26.setMaximumSize(QSize(55, 55))
        self.btn_26.setBaseSize(QSize(40, 40))
        self.btn_26.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.btn_26)

        self.btn_27 = QPushButton(self.wt_keyboard)
        self.btn_27.setObjectName(u"btn_27")
        sizePolicy4.setHeightForWidth(self.btn_27.sizePolicy().hasHeightForWidth())
        self.btn_27.setSizePolicy(sizePolicy4)
        self.btn_27.setMinimumSize(QSize(55, 55))
        self.btn_27.setMaximumSize(QSize(55, 55))
        self.btn_27.setBaseSize(QSize(40, 40))
        self.btn_27.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.btn_27)

        self.btn_28 = QPushButton(self.wt_keyboard)
        self.btn_28.setObjectName(u"btn_28")
        sizePolicy4.setHeightForWidth(self.btn_28.sizePolicy().hasHeightForWidth())
        self.btn_28.setSizePolicy(sizePolicy4)
        self.btn_28.setMinimumSize(QSize(55, 55))
        self.btn_28.setMaximumSize(QSize(55, 55))
        self.btn_28.setBaseSize(QSize(40, 40))
        self.btn_28.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.btn_28)

        self.btn_29 = QPushButton(self.wt_keyboard)
        self.btn_29.setObjectName(u"btn_29")
        sizePolicy4.setHeightForWidth(self.btn_29.sizePolicy().hasHeightForWidth())
        self.btn_29.setSizePolicy(sizePolicy4)
        self.btn_29.setMinimumSize(QSize(55, 55))
        self.btn_29.setMaximumSize(QSize(55, 55))
        self.btn_29.setBaseSize(QSize(40, 40))
        self.btn_29.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.btn_29)

        self.btn_30 = QPushButton(self.wt_keyboard)
        self.btn_30.setObjectName(u"btn_30")
        sizePolicy4.setHeightForWidth(self.btn_30.sizePolicy().hasHeightForWidth())
        self.btn_30.setSizePolicy(sizePolicy4)
        self.btn_30.setMinimumSize(QSize(55, 55))
        self.btn_30.setMaximumSize(QSize(55, 55))
        self.btn_30.setBaseSize(QSize(40, 40))
        self.btn_30.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.btn_30)

        self.btn_31 = QPushButton(self.wt_keyboard)
        self.btn_31.setObjectName(u"btn_31")
        sizePolicy4.setHeightForWidth(self.btn_31.sizePolicy().hasHeightForWidth())
        self.btn_31.setSizePolicy(sizePolicy4)
        self.btn_31.setMinimumSize(QSize(55, 55))
        self.btn_31.setMaximumSize(QSize(55, 55))
        self.btn_31.setBaseSize(QSize(40, 40))
        self.btn_31.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.btn_31)

        self.btn_32 = QPushButton(self.wt_keyboard)
        self.btn_32.setObjectName(u"btn_32")
        sizePolicy4.setHeightForWidth(self.btn_32.sizePolicy().hasHeightForWidth())
        self.btn_32.setSizePolicy(sizePolicy4)
        self.btn_32.setMinimumSize(QSize(55, 55))
        self.btn_32.setMaximumSize(QSize(55, 55))
        self.btn_32.setBaseSize(QSize(40, 40))
        self.btn_32.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.btn_32)

        self.btn_33 = QPushButton(self.wt_keyboard)
        self.btn_33.setObjectName(u"btn_33")
        sizePolicy4.setHeightForWidth(self.btn_33.sizePolicy().hasHeightForWidth())
        self.btn_33.setSizePolicy(sizePolicy4)
        self.btn_33.setMinimumSize(QSize(55, 55))
        self.btn_33.setMaximumSize(QSize(55, 55))
        self.btn_33.setBaseSize(QSize(40, 40))
        self.btn_33.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.btn_33)

        self.btn_rshift = QPushButton(self.wt_keyboard)
        self.btn_rshift.setObjectName(u"btn_rshift")
        sizePolicy6.setHeightForWidth(self.btn_rshift.sizePolicy().hasHeightForWidth())
        self.btn_rshift.setSizePolicy(sizePolicy6)
        self.btn_rshift.setMinimumSize(QSize(55, 55))
        self.btn_rshift.setMaximumSize(QSize(1000, 55))
        self.btn_rshift.setBaseSize(QSize(40, 40))
        self.btn_rshift.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.btn_rshift)


        self.lt_keyboard.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(9)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_56 = QPushButton(self.wt_keyboard)
        self.pushButton_56.setObjectName(u"pushButton_56")
        sizePolicy4.setHeightForWidth(self.pushButton_56.sizePolicy().hasHeightForWidth())
        self.pushButton_56.setSizePolicy(sizePolicy4)
        self.pushButton_56.setMinimumSize(QSize(69, 55))
        self.pushButton_56.setMaximumSize(QSize(55, 55))
        self.pushButton_56.setBaseSize(QSize(40, 40))
        self.pushButton_56.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_13.addWidget(self.pushButton_56)

        self.pushButton_57 = QPushButton(self.wt_keyboard)
        self.pushButton_57.setObjectName(u"pushButton_57")
        sizePolicy4.setHeightForWidth(self.pushButton_57.sizePolicy().hasHeightForWidth())
        self.pushButton_57.setSizePolicy(sizePolicy4)
        self.pushButton_57.setMinimumSize(QSize(69, 55))
        self.pushButton_57.setMaximumSize(QSize(55, 55))
        self.pushButton_57.setBaseSize(QSize(40, 40))
        self.pushButton_57.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_13.addWidget(self.pushButton_57)

        self.pushButton_58 = QPushButton(self.wt_keyboard)
        self.pushButton_58.setObjectName(u"pushButton_58")
        sizePolicy4.setHeightForWidth(self.pushButton_58.sizePolicy().hasHeightForWidth())
        self.pushButton_58.setSizePolicy(sizePolicy4)
        self.pushButton_58.setMinimumSize(QSize(69, 55))
        self.pushButton_58.setMaximumSize(QSize(55, 55))
        self.pushButton_58.setBaseSize(QSize(40, 40))
        self.pushButton_58.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_13.addWidget(self.pushButton_58)

        self.btn_space = QPushButton(self.wt_keyboard)
        self.btn_space.setObjectName(u"btn_space")
        sizePolicy6.setHeightForWidth(self.btn_space.sizePolicy().hasHeightForWidth())
        self.btn_space.setSizePolicy(sizePolicy6)
        self.btn_space.setMinimumSize(QSize(0, 55))
        self.btn_space.setMaximumSize(QSize(10000, 55))
        self.btn_space.setBaseSize(QSize(40, 40))
        self.btn_space.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_13.addWidget(self.btn_space)

        self.pushButton_60 = QPushButton(self.wt_keyboard)
        self.pushButton_60.setObjectName(u"pushButton_60")
        sizePolicy4.setHeightForWidth(self.pushButton_60.sizePolicy().hasHeightForWidth())
        self.pushButton_60.setSizePolicy(sizePolicy4)
        self.pushButton_60.setMinimumSize(QSize(69, 55))
        self.pushButton_60.setMaximumSize(QSize(55, 55))
        self.pushButton_60.setBaseSize(QSize(40, 40))
        self.pushButton_60.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_13.addWidget(self.pushButton_60)

        self.pushButton_61 = QPushButton(self.wt_keyboard)
        self.pushButton_61.setObjectName(u"pushButton_61")
        sizePolicy4.setHeightForWidth(self.pushButton_61.sizePolicy().hasHeightForWidth())
        self.pushButton_61.setSizePolicy(sizePolicy4)
        self.pushButton_61.setMinimumSize(QSize(69, 55))
        self.pushButton_61.setMaximumSize(QSize(55, 55))
        self.pushButton_61.setBaseSize(QSize(40, 40))
        self.pushButton_61.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_13.addWidget(self.pushButton_61)

        self.pushButton_62 = QPushButton(self.wt_keyboard)
        self.pushButton_62.setObjectName(u"pushButton_62")
        sizePolicy4.setHeightForWidth(self.pushButton_62.sizePolicy().hasHeightForWidth())
        self.pushButton_62.setSizePolicy(sizePolicy4)
        self.pushButton_62.setMinimumSize(QSize(69, 55))
        self.pushButton_62.setMaximumSize(QSize(55, 55))
        self.pushButton_62.setBaseSize(QSize(40, 40))
        self.pushButton_62.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_13.addWidget(self.pushButton_62)

        self.pushButton_63 = QPushButton(self.wt_keyboard)
        self.pushButton_63.setObjectName(u"pushButton_63")
        sizePolicy4.setHeightForWidth(self.pushButton_63.sizePolicy().hasHeightForWidth())
        self.pushButton_63.setSizePolicy(sizePolicy4)
        self.pushButton_63.setMinimumSize(QSize(69, 55))
        self.pushButton_63.setMaximumSize(QSize(55, 55))
        self.pushButton_63.setBaseSize(QSize(40, 40))
        self.pushButton_63.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_13.addWidget(self.pushButton_63)


        self.lt_keyboard.addLayout(self.horizontalLayout_13)


        self.verticalLayout_8.addWidget(self.wt_keyboard)


        self.horizontalLayout_2.addWidget(self.verticalWidget, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_entry.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span>\u0432\u044b\u0430\u044bdsfsd</span></p></body></html>", None))
        self.lbl_wpm.setText(QCoreApplication.translate("MainWindow", u"WPM 30", None))
        self.lbl_accuracy.setText(QCoreApplication.translate("MainWindow", u"Accuracy 95%", None))
        self.lbl_spacer_2.setText("")
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"`", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_52.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn_backspace.setText(QCoreApplication.translate("MainWindow", u"Backspace", None))
        self.btn_tab.setText(QCoreApplication.translate("MainWindow", u"Tab", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"q", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"w", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"e", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"r", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"t", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"u", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"o", None))
        self.btn_10.setText(QCoreApplication.translate("MainWindow", u"p", None))
        self.btn_11.setText(QCoreApplication.translate("MainWindow", u"[", None))
        self.btn_12.setText(QCoreApplication.translate("MainWindow", u"]", None))
        self.btn_backslash.setText(QCoreApplication.translate("MainWindow", u"\\", None))
        self.btn_caps.setText(QCoreApplication.translate("MainWindow", u"Caps", None))
        self.btn_13.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.btn_14.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.btn_15.setText(QCoreApplication.translate("MainWindow", u"d", None))
        self.btn_16.setText(QCoreApplication.translate("MainWindow", u"f", None))
        self.btn_17.setText(QCoreApplication.translate("MainWindow", u"g", None))
        self.btn_18.setText(QCoreApplication.translate("MainWindow", u"h", None))
        self.btn_19.setText(QCoreApplication.translate("MainWindow", u"j", None))
        self.btn_20.setText(QCoreApplication.translate("MainWindow", u"k", None))
        self.btn_21.setText(QCoreApplication.translate("MainWindow", u"l", None))
        self.btn_22.setText(QCoreApplication.translate("MainWindow", u";", None))
        self.btn_23.setText(QCoreApplication.translate("MainWindow", u"'", None))
        self.btn_enter.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.btn_lshift.setText(QCoreApplication.translate("MainWindow", u"Shift", None))
        self.btn_24.setText(QCoreApplication.translate("MainWindow", u"z", None))
        self.btn_25.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.btn_26.setText(QCoreApplication.translate("MainWindow", u"c", None))
        self.btn_27.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.btn_28.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.btn_29.setText(QCoreApplication.translate("MainWindow", u"n", None))
        self.btn_30.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.btn_31.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.btn_32.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btn_33.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.btn_rshift.setText(QCoreApplication.translate("MainWindow", u"Shift", None))
        self.pushButton_56.setText(QCoreApplication.translate("MainWindow", u"Ctrl", None))
        self.pushButton_57.setText(QCoreApplication.translate("MainWindow", u"Win", None))
        self.pushButton_58.setText(QCoreApplication.translate("MainWindow", u"Alt", None))
        self.btn_space.setText(QCoreApplication.translate("MainWindow", u"Space", None))
        self.pushButton_60.setText(QCoreApplication.translate("MainWindow", u"Alt", None))
        self.pushButton_61.setText(QCoreApplication.translate("MainWindow", u"Fn", None))
        self.pushButton_62.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.pushButton_63.setText(QCoreApplication.translate("MainWindow", u"Ctrl", None))
    # retranslateUi

