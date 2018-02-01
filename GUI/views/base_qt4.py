# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layouts/base.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_Graph = QtGui.QVBoxLayout()
        self.verticalLayout_Graph.setObjectName(_fromUtf8("verticalLayout_Graph"))
        self.graph = PlotWidget(self.centralwidget)
        self.graph.setObjectName(_fromUtf8("graph"))
        self.verticalLayout_Graph.addWidget(self.graph)
        self.lbl_StatusGraph = QtGui.QLabel(self.centralwidget)
        self.lbl_StatusGraph.setObjectName(_fromUtf8("lbl_StatusGraph"))
        self.verticalLayout_Graph.addWidget(self.lbl_StatusGraph)
        self.horizontalLayout_2.addLayout(self.verticalLayout_Graph)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_Options = QtGui.QDockWidget(MainWindow)
        self.dockWidget_Options.setMinimumSize(QtCore.QSize(128, 145))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.dockWidget_Options.setFont(font)
        self.dockWidget_Options.setFloating(False)
        self.dockWidget_Options.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.dockWidget_Options.setObjectName(_fromUtf8("dockWidget_Options"))
        self.dockWidgetContents_Options = QtGui.QWidget()
        self.dockWidgetContents_Options.setObjectName(_fromUtf8("dockWidgetContents_Options"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents_Options)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnStart = QtGui.QPushButton(self.dockWidgetContents_Options)
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.verticalLayout.addWidget(self.btnStart)
        self.btnA = QtGui.QPushButton(self.dockWidgetContents_Options)
        self.btnA.setObjectName(_fromUtf8("btnA"))
        self.verticalLayout.addWidget(self.btnA)
        self.btnB = QtGui.QPushButton(self.dockWidgetContents_Options)
        self.btnB.setObjectName(_fromUtf8("btnB"))
        self.verticalLayout.addWidget(self.btnB)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.dockWidget_Options.setWidget(self.dockWidgetContents_Options)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_Options)
        self.dockWidget_Communication = QtGui.QDockWidget(MainWindow)
        self.dockWidget_Communication.setEnabled(True)
        self.dockWidget_Communication.setFloating(False)
        self.dockWidget_Communication.setObjectName(_fromUtf8("dockWidget_Communication"))
        self.dockWidgetContents_Com = QtGui.QWidget()
        self.dockWidgetContents_Com.setObjectName(_fromUtf8("dockWidgetContents_Com"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents_Com)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lblSerialPortTitle = QtGui.QLabel(self.dockWidgetContents_Com)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblSerialPortTitle.setFont(font)
        self.lblSerialPortTitle.setObjectName(_fromUtf8("lblSerialPortTitle"))
        self.verticalLayout_2.addWidget(self.lblSerialPortTitle)
        self.cbSerialPort = QtGui.QComboBox(self.dockWidgetContents_Com)
        self.cbSerialPort.setObjectName(_fromUtf8("cbSerialPort"))
        self.verticalLayout_2.addWidget(self.cbSerialPort)
        self.cbBaudRates = QtGui.QComboBox(self.dockWidgetContents_Com)
        self.cbBaudRates.setObjectName(_fromUtf8("cbBaudRates"))
        self.verticalLayout_2.addWidget(self.cbBaudRates)
        self.btnConnect = QtGui.QPushButton(self.dockWidgetContents_Com)
        self.btnConnect.setObjectName(_fromUtf8("btnConnect"))
        self.verticalLayout_2.addWidget(self.btnConnect)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.dockWidget_Communication.setWidget(self.dockWidgetContents_Com)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_Communication)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionTutorial = QtGui.QAction(MainWindow)
        self.actionTutorial.setObjectName(_fromUtf8("actionTutorial"))
        self.actionOptions_Menu = QtGui.QAction(MainWindow)
        self.actionOptions_Menu.setCheckable(True)
        self.actionOptions_Menu.setChecked(True)
        self.actionOptions_Menu.setObjectName(_fromUtf8("actionOptions_Menu"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionCommunication_Menu = QtGui.QAction(MainWindow)
        self.actionCommunication_Menu.setCheckable(True)
        self.actionCommunication_Menu.setChecked(True)
        self.actionCommunication_Menu.setObjectName(_fromUtf8("actionCommunication_Menu"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuView.addAction(self.actionOptions_Menu)
        self.menuView.addAction(self.actionCommunication_Menu)
        self.menuHelp.addAction(self.actionTutorial)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.graph, self.btnStart)
        MainWindow.setTabOrder(self.btnStart, self.btnA)
        MainWindow.setTabOrder(self.btnA, self.btnB)
        MainWindow.setTabOrder(self.btnB, self.cbSerialPort)
        MainWindow.setTabOrder(self.cbSerialPort, self.cbBaudRates)
        MainWindow.setTabOrder(self.cbBaudRates, self.btnConnect)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Real Time Gait Tracking", None))
        self.lbl_StatusGraph.setText(_translate("MainWindow", "Status Buffers:", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.dockWidget_Options.setWindowTitle(_translate("MainWindow", "Options", None))
        self.btnStart.setText(_translate("MainWindow", "S", None))
        self.btnA.setText(_translate("MainWindow", "A", None))
        self.btnB.setText(_translate("MainWindow", "B", None))
        self.dockWidget_Communication.setWindowTitle(_translate("MainWindow", "Communication", None))
        self.lblSerialPortTitle.setText(_translate("MainWindow", "Porta Serial:", None))
        self.btnConnect.setText(_translate("MainWindow", "Connect", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionTutorial.setText(_translate("MainWindow", "Help", None))
        self.actionOptions_Menu.setText(_translate("MainWindow", "Options Menu", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionCommunication_Menu.setText(_translate("MainWindow", "Communication Menu", None))

from pyqtgraph import PlotWidget
