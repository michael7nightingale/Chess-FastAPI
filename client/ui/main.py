from PyQt6 import QtCore, QtWidgets, QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(parent=self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtGui.QAction(parent=MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionRules = QtGui.QAction(parent=MainWindow)
        self.actionRules.setObjectName("actionRules")
        self.menuSettings.addAction(self.actionSettings)
        self.menuSettings.addAction(self.actionRules)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionRules.setText(_translate("MainWindow", "Rules"))
