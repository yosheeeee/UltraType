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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1055, 536)
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
        self.verticalWidget = QWidget(self.centralwidget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
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
"font-weight: 400;")
        self.lbl_entry.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

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

        self.wt_keyboard = QWidget(self.verticalWidget)
        self.wt_keyboard.setObjectName(u"wt_keyboard")
        self.wt_keyboard.setEnabled(True)
        self.lt_keyboard = QVBoxLayout(self.wt_keyboard)
        self.lt_keyboard.setSpacing(9)
        self.lt_keyboard.setObjectName(u"lt_keyboard")
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

        self.btn_q = QPushButton(self.wt_keyboard)
        self.btn_q.setObjectName(u"btn_q")
        sizePolicy4.setHeightForWidth(self.btn_q.sizePolicy().hasHeightForWidth())
        self.btn_q.setSizePolicy(sizePolicy4)
        self.btn_q.setMinimumSize(QSize(55, 55))
        self.btn_q.setMaximumSize(QSize(55, 55))
        self.btn_q.setBaseSize(QSize(40, 40))
        self.btn_q.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_q)

        self.btn_w = QPushButton(self.wt_keyboard)
        self.btn_w.setObjectName(u"btn_w")
        sizePolicy4.setHeightForWidth(self.btn_w.sizePolicy().hasHeightForWidth())
        self.btn_w.setSizePolicy(sizePolicy4)
        self.btn_w.setMinimumSize(QSize(55, 55))
        self.btn_w.setMaximumSize(QSize(55, 55))
        self.btn_w.setBaseSize(QSize(40, 40))
        self.btn_w.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_w)

        self.btn_e = QPushButton(self.wt_keyboard)
        self.btn_e.setObjectName(u"btn_e")
        sizePolicy4.setHeightForWidth(self.btn_e.sizePolicy().hasHeightForWidth())
        self.btn_e.setSizePolicy(sizePolicy4)
        self.btn_e.setMinimumSize(QSize(55, 55))
        self.btn_e.setMaximumSize(QSize(55, 55))
        self.btn_e.setBaseSize(QSize(40, 40))
        self.btn_e.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_e)

        self.btn_r = QPushButton(self.wt_keyboard)
        self.btn_r.setObjectName(u"btn_r")
        sizePolicy4.setHeightForWidth(self.btn_r.sizePolicy().hasHeightForWidth())
        self.btn_r.setSizePolicy(sizePolicy4)
        self.btn_r.setMinimumSize(QSize(55, 55))
        self.btn_r.setMaximumSize(QSize(55, 55))
        self.btn_r.setBaseSize(QSize(40, 40))
        self.btn_r.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_r)

        self.btn_t = QPushButton(self.wt_keyboard)
        self.btn_t.setObjectName(u"btn_t")
        sizePolicy4.setHeightForWidth(self.btn_t.sizePolicy().hasHeightForWidth())
        self.btn_t.setSizePolicy(sizePolicy4)
        self.btn_t.setMinimumSize(QSize(55, 55))
        self.btn_t.setMaximumSize(QSize(55, 55))
        self.btn_t.setBaseSize(QSize(40, 40))
        self.btn_t.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_t)

        self.btn_y = QPushButton(self.wt_keyboard)
        self.btn_y.setObjectName(u"btn_y")
        sizePolicy4.setHeightForWidth(self.btn_y.sizePolicy().hasHeightForWidth())
        self.btn_y.setSizePolicy(sizePolicy4)
        self.btn_y.setMinimumSize(QSize(55, 55))
        self.btn_y.setMaximumSize(QSize(55, 55))
        self.btn_y.setBaseSize(QSize(40, 40))
        self.btn_y.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_y)

        self.btn_u = QPushButton(self.wt_keyboard)
        self.btn_u.setObjectName(u"btn_u")
        sizePolicy4.setHeightForWidth(self.btn_u.sizePolicy().hasHeightForWidth())
        self.btn_u.setSizePolicy(sizePolicy4)
        self.btn_u.setMinimumSize(QSize(55, 55))
        self.btn_u.setMaximumSize(QSize(55, 55))
        self.btn_u.setBaseSize(QSize(40, 40))
        self.btn_u.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_u)

        self.btn_i = QPushButton(self.wt_keyboard)
        self.btn_i.setObjectName(u"btn_i")
        sizePolicy4.setHeightForWidth(self.btn_i.sizePolicy().hasHeightForWidth())
        self.btn_i.setSizePolicy(sizePolicy4)
        self.btn_i.setMinimumSize(QSize(55, 55))
        self.btn_i.setMaximumSize(QSize(55, 55))
        self.btn_i.setBaseSize(QSize(40, 40))
        self.btn_i.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_i)

        self.btn_o = QPushButton(self.wt_keyboard)
        self.btn_o.setObjectName(u"btn_o")
        sizePolicy4.setHeightForWidth(self.btn_o.sizePolicy().hasHeightForWidth())
        self.btn_o.setSizePolicy(sizePolicy4)
        self.btn_o.setMinimumSize(QSize(55, 55))
        self.btn_o.setMaximumSize(QSize(55, 55))
        self.btn_o.setBaseSize(QSize(40, 40))
        self.btn_o.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_o)

        self.btn_p = QPushButton(self.wt_keyboard)
        self.btn_p.setObjectName(u"btn_p")
        sizePolicy4.setHeightForWidth(self.btn_p.sizePolicy().hasHeightForWidth())
        self.btn_p.setSizePolicy(sizePolicy4)
        self.btn_p.setMinimumSize(QSize(55, 55))
        self.btn_p.setMaximumSize(QSize(55, 55))
        self.btn_p.setBaseSize(QSize(40, 40))
        self.btn_p.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_p)

        self.btn_openbracket = QPushButton(self.wt_keyboard)
        self.btn_openbracket.setObjectName(u"btn_openbracket")
        sizePolicy4.setHeightForWidth(self.btn_openbracket.sizePolicy().hasHeightForWidth())
        self.btn_openbracket.setSizePolicy(sizePolicy4)
        self.btn_openbracket.setMinimumSize(QSize(55, 55))
        self.btn_openbracket.setMaximumSize(QSize(55, 55))
        self.btn_openbracket.setBaseSize(QSize(40, 40))
        self.btn_openbracket.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_openbracket)

        self.btn_closebracket = QPushButton(self.wt_keyboard)
        self.btn_closebracket.setObjectName(u"btn_closebracket")
        sizePolicy4.setHeightForWidth(self.btn_closebracket.sizePolicy().hasHeightForWidth())
        self.btn_closebracket.setSizePolicy(sizePolicy4)
        self.btn_closebracket.setMinimumSize(QSize(55, 55))
        self.btn_closebracket.setMaximumSize(QSize(55, 55))
        self.btn_closebracket.setBaseSize(QSize(40, 40))
        self.btn_closebracket.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.btn_closebracket)

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

        self.btn_a = QPushButton(self.wt_keyboard)
        self.btn_a.setObjectName(u"btn_a")
        sizePolicy4.setHeightForWidth(self.btn_a.sizePolicy().hasHeightForWidth())
        self.btn_a.setSizePolicy(sizePolicy4)
        self.btn_a.setMinimumSize(QSize(55, 55))
        self.btn_a.setMaximumSize(QSize(55, 55))
        self.btn_a.setBaseSize(QSize(40, 40))
        self.btn_a.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_a)

        self.btn_s = QPushButton(self.wt_keyboard)
        self.btn_s.setObjectName(u"btn_s")
        sizePolicy4.setHeightForWidth(self.btn_s.sizePolicy().hasHeightForWidth())
        self.btn_s.setSizePolicy(sizePolicy4)
        self.btn_s.setMinimumSize(QSize(55, 55))
        self.btn_s.setMaximumSize(QSize(55, 55))
        self.btn_s.setBaseSize(QSize(40, 40))
        self.btn_s.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_s)

        self.btn_d = QPushButton(self.wt_keyboard)
        self.btn_d.setObjectName(u"btn_d")
        sizePolicy4.setHeightForWidth(self.btn_d.sizePolicy().hasHeightForWidth())
        self.btn_d.setSizePolicy(sizePolicy4)
        self.btn_d.setMinimumSize(QSize(55, 55))
        self.btn_d.setMaximumSize(QSize(55, 55))
        self.btn_d.setBaseSize(QSize(40, 40))
        self.btn_d.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_d)

        self.btn_f = QPushButton(self.wt_keyboard)
        self.btn_f.setObjectName(u"btn_f")
        sizePolicy4.setHeightForWidth(self.btn_f.sizePolicy().hasHeightForWidth())
        self.btn_f.setSizePolicy(sizePolicy4)
        self.btn_f.setMinimumSize(QSize(55, 55))
        self.btn_f.setMaximumSize(QSize(55, 55))
        self.btn_f.setBaseSize(QSize(40, 40))
        self.btn_f.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_f)

        self.btn_g = QPushButton(self.wt_keyboard)
        self.btn_g.setObjectName(u"btn_g")
        sizePolicy4.setHeightForWidth(self.btn_g.sizePolicy().hasHeightForWidth())
        self.btn_g.setSizePolicy(sizePolicy4)
        self.btn_g.setMinimumSize(QSize(55, 55))
        self.btn_g.setMaximumSize(QSize(55, 55))
        self.btn_g.setBaseSize(QSize(40, 40))
        self.btn_g.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_g)

        self.btn_h = QPushButton(self.wt_keyboard)
        self.btn_h.setObjectName(u"btn_h")
        sizePolicy4.setHeightForWidth(self.btn_h.sizePolicy().hasHeightForWidth())
        self.btn_h.setSizePolicy(sizePolicy4)
        self.btn_h.setMinimumSize(QSize(55, 55))
        self.btn_h.setMaximumSize(QSize(55, 55))
        self.btn_h.setBaseSize(QSize(40, 40))
        self.btn_h.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_h)

        self.btn_j = QPushButton(self.wt_keyboard)
        self.btn_j.setObjectName(u"btn_j")
        sizePolicy4.setHeightForWidth(self.btn_j.sizePolicy().hasHeightForWidth())
        self.btn_j.setSizePolicy(sizePolicy4)
        self.btn_j.setMinimumSize(QSize(55, 55))
        self.btn_j.setMaximumSize(QSize(55, 55))
        self.btn_j.setBaseSize(QSize(40, 40))
        self.btn_j.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_j)

        self.btn_k = QPushButton(self.wt_keyboard)
        self.btn_k.setObjectName(u"btn_k")
        sizePolicy4.setHeightForWidth(self.btn_k.sizePolicy().hasHeightForWidth())
        self.btn_k.setSizePolicy(sizePolicy4)
        self.btn_k.setMinimumSize(QSize(55, 55))
        self.btn_k.setMaximumSize(QSize(55, 55))
        self.btn_k.setBaseSize(QSize(40, 40))
        self.btn_k.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_k)

        self.btn_l = QPushButton(self.wt_keyboard)
        self.btn_l.setObjectName(u"btn_l")
        sizePolicy4.setHeightForWidth(self.btn_l.sizePolicy().hasHeightForWidth())
        self.btn_l.setSizePolicy(sizePolicy4)
        self.btn_l.setMinimumSize(QSize(55, 55))
        self.btn_l.setMaximumSize(QSize(55, 55))
        self.btn_l.setBaseSize(QSize(40, 40))
        self.btn_l.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.btn_l)

        self.pushButton_29 = QPushButton(self.wt_keyboard)
        self.pushButton_29.setObjectName(u"pushButton_29")
        sizePolicy4.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy4)
        self.pushButton_29.setMinimumSize(QSize(55, 55))
        self.pushButton_29.setMaximumSize(QSize(55, 55))
        self.pushButton_29.setBaseSize(QSize(40, 40))
        self.pushButton_29.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.pushButton_29)

        self.pushButton_28 = QPushButton(self.wt_keyboard)
        self.pushButton_28.setObjectName(u"pushButton_28")
        sizePolicy4.setHeightForWidth(self.pushButton_28.sizePolicy().hasHeightForWidth())
        self.pushButton_28.setSizePolicy(sizePolicy4)
        self.pushButton_28.setMinimumSize(QSize(55, 55))
        self.pushButton_28.setMaximumSize(QSize(55, 55))
        self.pushButton_28.setBaseSize(QSize(40, 40))
        self.pushButton_28.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.pushButton_28)

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

        self.btn_z = QPushButton(self.wt_keyboard)
        self.btn_z.setObjectName(u"btn_z")
        sizePolicy4.setHeightForWidth(self.btn_z.sizePolicy().hasHeightForWidth())
        self.btn_z.setSizePolicy(sizePolicy4)
        self.btn_z.setMinimumSize(QSize(55, 55))
        self.btn_z.setMaximumSize(QSize(55, 55))
        self.btn_z.setBaseSize(QSize(40, 40))
        self.btn_z.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.btn_z)

        self.btn_x = QPushButton(self.wt_keyboard)
        self.btn_x.setObjectName(u"btn_x")
        sizePolicy4.setHeightForWidth(self.btn_x.sizePolicy().hasHeightForWidth())
        self.btn_x.setSizePolicy(sizePolicy4)
        self.btn_x.setMinimumSize(QSize(55, 55))
        self.btn_x.setMaximumSize(QSize(55, 55))
        self.btn_x.setBaseSize(QSize(40, 40))
        self.btn_x.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.btn_x)

        self.btn_c = QPushButton(self.wt_keyboard)
        self.btn_c.setObjectName(u"btn_c")
        sizePolicy4.setHeightForWidth(self.btn_c.sizePolicy().hasHeightForWidth())
        self.btn_c.setSizePolicy(sizePolicy4)
        self.btn_c.setMinimumSize(QSize(55, 55))
        self.btn_c.setMaximumSize(QSize(55, 55))
        self.btn_c.setBaseSize(QSize(40, 40))
        self.btn_c.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.btn_c)

        self.btn_v = QPushButton(self.wt_keyboard)
        self.btn_v.setObjectName(u"btn_v")
        sizePolicy4.setHeightForWidth(self.btn_v.sizePolicy().hasHeightForWidth())
        self.btn_v.setSizePolicy(sizePolicy4)
        self.btn_v.setMinimumSize(QSize(55, 55))
        self.btn_v.setMaximumSize(QSize(55, 55))
        self.btn_v.setBaseSize(QSize(40, 40))
        self.btn_v.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.btn_v)

        self.btn_b = QPushButton(self.wt_keyboard)
        self.btn_b.setObjectName(u"btn_b")
        sizePolicy4.setHeightForWidth(self.btn_b.sizePolicy().hasHeightForWidth())
        self.btn_b.setSizePolicy(sizePolicy4)
        self.btn_b.setMinimumSize(QSize(55, 55))
        self.btn_b.setMaximumSize(QSize(55, 55))
        self.btn_b.setBaseSize(QSize(40, 40))
        self.btn_b.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.btn_b)

        self.btn_n = QPushButton(self.wt_keyboard)
        self.btn_n.setObjectName(u"btn_n")
        sizePolicy4.setHeightForWidth(self.btn_n.sizePolicy().hasHeightForWidth())
        self.btn_n.setSizePolicy(sizePolicy4)
        self.btn_n.setMinimumSize(QSize(55, 55))
        self.btn_n.setMaximumSize(QSize(55, 55))
        self.btn_n.setBaseSize(QSize(40, 40))
        self.btn_n.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.btn_n)

        self.btn_m = QPushButton(self.wt_keyboard)
        self.btn_m.setObjectName(u"btn_m")
        sizePolicy4.setHeightForWidth(self.btn_m.sizePolicy().hasHeightForWidth())
        self.btn_m.setSizePolicy(sizePolicy4)
        self.btn_m.setMinimumSize(QSize(55, 55))
        self.btn_m.setMaximumSize(QSize(55, 55))
        self.btn_m.setBaseSize(QSize(40, 40))
        self.btn_m.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.btn_m)

        self.pushButton_42 = QPushButton(self.wt_keyboard)
        self.pushButton_42.setObjectName(u"pushButton_42")
        sizePolicy4.setHeightForWidth(self.pushButton_42.sizePolicy().hasHeightForWidth())
        self.pushButton_42.setSizePolicy(sizePolicy4)
        self.pushButton_42.setMinimumSize(QSize(55, 55))
        self.pushButton_42.setMaximumSize(QSize(55, 55))
        self.pushButton_42.setBaseSize(QSize(40, 40))
        self.pushButton_42.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.pushButton_42)

        self.pushButton_41 = QPushButton(self.wt_keyboard)
        self.pushButton_41.setObjectName(u"pushButton_41")
        sizePolicy4.setHeightForWidth(self.pushButton_41.sizePolicy().hasHeightForWidth())
        self.pushButton_41.setSizePolicy(sizePolicy4)
        self.pushButton_41.setMinimumSize(QSize(55, 55))
        self.pushButton_41.setMaximumSize(QSize(55, 55))
        self.pushButton_41.setBaseSize(QSize(40, 40))
        self.pushButton_41.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.pushButton_41)

        self.pushButton_64 = QPushButton(self.wt_keyboard)
        self.pushButton_64.setObjectName(u"pushButton_64")
        sizePolicy4.setHeightForWidth(self.pushButton_64.sizePolicy().hasHeightForWidth())
        self.pushButton_64.setSizePolicy(sizePolicy4)
        self.pushButton_64.setMinimumSize(QSize(55, 55))
        self.pushButton_64.setMaximumSize(QSize(55, 55))
        self.pushButton_64.setBaseSize(QSize(40, 40))
        self.pushButton_64.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.pushButton_64)

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
        self.lbl_entry.setText(QCoreApplication.translate("MainWindow", u"\u0432\u044b\u0430\u044b\u0432", None))
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
        self.btn_q.setText(QCoreApplication.translate("MainWindow", u"q", None))
        self.btn_w.setText(QCoreApplication.translate("MainWindow", u"w", None))
        self.btn_e.setText(QCoreApplication.translate("MainWindow", u"e", None))
        self.btn_r.setText(QCoreApplication.translate("MainWindow", u"r", None))
        self.btn_t.setText(QCoreApplication.translate("MainWindow", u"t", None))
        self.btn_y.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.btn_u.setText(QCoreApplication.translate("MainWindow", u"u", None))
        self.btn_i.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.btn_o.setText(QCoreApplication.translate("MainWindow", u"o", None))
        self.btn_p.setText(QCoreApplication.translate("MainWindow", u"p", None))
        self.btn_openbracket.setText(QCoreApplication.translate("MainWindow", u"[", None))
        self.btn_closebracket.setText(QCoreApplication.translate("MainWindow", u"]", None))
        self.btn_backslash.setText(QCoreApplication.translate("MainWindow", u"\\", None))
        self.btn_caps.setText(QCoreApplication.translate("MainWindow", u"Caps", None))
        self.btn_a.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.btn_s.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.btn_d.setText(QCoreApplication.translate("MainWindow", u"d", None))
        self.btn_f.setText(QCoreApplication.translate("MainWindow", u"f", None))
        self.btn_g.setText(QCoreApplication.translate("MainWindow", u"g", None))
        self.btn_h.setText(QCoreApplication.translate("MainWindow", u"h", None))
        self.btn_j.setText(QCoreApplication.translate("MainWindow", u"j", None))
        self.btn_k.setText(QCoreApplication.translate("MainWindow", u"k", None))
        self.btn_l.setText(QCoreApplication.translate("MainWindow", u"l", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u";", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"'", None))
        self.btn_enter.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.btn_lshift.setText(QCoreApplication.translate("MainWindow", u"Shift", None))
        self.btn_z.setText(QCoreApplication.translate("MainWindow", u"z", None))
        self.btn_x.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.btn_c.setText(QCoreApplication.translate("MainWindow", u"c", None))
        self.btn_v.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.btn_b.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.btn_n.setText(QCoreApplication.translate("MainWindow", u"n", None))
        self.btn_m.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_64.setText(QCoreApplication.translate("MainWindow", u"/", None))
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

