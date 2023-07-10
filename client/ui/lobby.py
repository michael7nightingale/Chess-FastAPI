from PyQt6 import QtCore, QtWidgets


class Ui_LobbyWindow(object):
    def setupUi(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.start_self_game_button = QtWidgets.QPushButton(parent=self.frame_3)
        self.start_self_game_button.setObjectName("start_self_game_button")
        self.verticalLayout_2.addWidget(self.start_self_game_button)

        self.join_game_button = QtWidgets.QPushButton(parent=self.frame_3)
        self.join_game_button.setObjectName("join_game_button")
        self.verticalLayout_2.addWidget(self.join_game_button)

        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        self.label.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.listWidget = QtWidgets.QListWidget(parent=self.frame_2)
        self.listWidget.setMaximumSize(QtCore.QSize(123123, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chess Game"))
        self.start_self_game_button.setText(_translate("MainWindow", "Start self game"))
        self.join_game_button.setText(_translate("MainWindow", "Join game"))
        self.label.setText(_translate("MainWindow", "Players"))
