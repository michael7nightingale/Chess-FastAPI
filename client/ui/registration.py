from PyQt6 import QtCore, QtWidgets


class Ui_RegistrationWindow(object):
    def setupUi(self, RegistrationWindow):
        RegistrationWindow.setObjectName("RegistrationWindow")
        RegistrationWindow.resize(378, 442)
        RegistrationWindow.setMinimumSize(QtCore.QSize(378, 442))
        RegistrationWindow.setMaximumSize(QtCore.QSize(378, 442))
        self.verticalLayout = QtWidgets.QVBoxLayout(RegistrationWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_frame = QtWidgets.QFrame(parent=RegistrationWindow)
        self.main_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.input_frame = QtWidgets.QFrame(parent=self.main_frame)
        self.input_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.input_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.input_frame.setObjectName("input_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.input_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame = QtWidgets.QFrame(parent=self.input_frame)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.username_input = QtWidgets.QLineEdit(parent=self.frame)
        self.username_input.setMinimumSize(QtCore.QSize(0, 30))
        self.username_input.setObjectName("username_input")
        self.verticalLayout_3.addWidget(self.username_input)
        self.username_label = QtWidgets.QLabel(parent=self.frame)
        self.username_label.setMaximumSize(QtCore.QSize(16777215, 18))
        self.username_label.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.username_label.setObjectName("username_label")
        self.verticalLayout_3.addWidget(self.username_label)
        self.verticalLayout_5.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=self.input_frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.password_input = QtWidgets.QLineEdit(parent=self.frame_2)
        self.password_input.setMinimumSize(QtCore.QSize(0, 30))
        self.password_input.setObjectName("password_input")
        self.verticalLayout_4.addWidget(self.password_input)
        self.password_label = QtWidgets.QLabel(parent=self.frame_2)
        self.password_label.setMaximumSize(QtCore.QSize(16777215, 18))
        self.password_label.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.password_label.setObjectName("password_label")
        self.verticalLayout_4.addWidget(self.password_label)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=self.input_frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.email_input = QtWidgets.QLineEdit(parent=self.frame_3)
        self.email_input.setMinimumSize(QtCore.QSize(0, 30))
        self.email_input.setObjectName("email_input")
        self.verticalLayout_9.addWidget(self.email_input)
        self.email_label = QtWidgets.QLabel(parent=self.frame_3)
        self.email_label.setMaximumSize(QtCore.QSize(16777215, 18))
        self.email_label.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.email_label.setObjectName("email_label")
        self.verticalLayout_9.addWidget(self.email_label)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.verticalLayout_2.addWidget(self.input_frame)
        self.submi_frame = QtWidgets.QFrame(parent=self.main_frame)
        self.submi_frame.setMinimumSize(QtCore.QSize(0, 70))
        self.submi_frame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.submi_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.submi_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.submi_frame.setObjectName("submi_frame")
        self.submit_button = QtWidgets.QPushButton(parent=self.submi_frame)
        self.submit_button.setGeometry(QtCore.QRect(110, 10, 131, 41))
        self.submit_button.setObjectName("submit_button")
        self.login_button = QtWidgets.QCommandLinkButton(parent=self.submi_frame)
        self.login_button.setGeometry(QtCore.QRect(250, 10, 101, 41))
        self.login_button.setObjectName("login_button")
        self.verticalLayout_2.addWidget(self.submi_frame)
        self.verticalLayout.addWidget(self.main_frame)

        self.retranslateUi(RegistrationWindow)
        QtCore.QMetaObject.connectSlotsByName(RegistrationWindow)

    def retranslateUi(self, RegistrationWindow):
        _translate = QtCore.QCoreApplication.translate
        RegistrationWindow.setWindowTitle(_translate("RegistrationWindow", "Login"))
        self.username_input.setPlaceholderText(_translate("RegistrationWindow", "Username:"))
        self.username_label.setText(_translate("RegistrationWindow", "TextLabel"))
        self.password_input.setPlaceholderText(_translate("RegistrationWindow", "Password:"))
        self.password_label.setText(_translate("RegistrationWindow", "TextLabel"))
        self.email_input.setPlaceholderText(_translate("RegistrationWindow", "Email:"))
        self.email_label.setText(_translate("RegistrationWindow", "TextLabel"))
        self.submit_button.setText(_translate("RegistrationWindow", "Register"))
        self.login_button.setText(_translate("RegistrationWindow", "Login"))