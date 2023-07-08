import requests
from PyQt6.QtWidgets import QWidget
from typing import Mapping

from ui.registration import Ui_RegistrationWindow
from validators import validate_password, validate_username, validate_email
from qt_tools import alert, show_exit_dialog


class RegistrationWindow(QWidget):
    def __init__(self, parent, config: Mapping):
        self.config = config
        self.main_window = parent
        super().__init__(parent=None)
        self.ui = Ui_RegistrationWindow()
        self.ui.setupUi(self)

        self.ui.submit_button.clicked.connect(self.onsubmit)
        self.ui.login_button.clicked.connect(self.onlogin)
        self.hide_labels()

    def hide_labels(self):
        self.ui.password_label.hide()
        self.ui.username_label.hide()
        self.ui.email_label.hide()

    def onsubmit(self, event):
        were_alerts = False
        username = self.ui.username_input.text()
        if not validate_username(username):
            alert(self.ui.username_label, "Username is invalid")
            were_alerts = True

        password = self.ui.password_input.text()
        if not validate_password(password):
            alert(self.ui.password_label, "Password is invalid")
            were_alerts = True

        email = self.ui.email_input.text()
        if not validate_email(email):
            alert(self.ui.email_label, "Email is invalid")
            were_alerts = True

        if not were_alerts:
            try:
                data = {
                    "username": username,
                    "password": password,
                    "email": email
                }
                response = requests.post(
                    self.config["base_url"] + "auth/register",
                    json=data
                )
                assert response.status_code == 201
            except requests.ConnectionError:
                show_exit_dialog(self, "Cannot connect to the server.")
            except AssertionError:
                print(response.json())
                show_exit_dialog(self, "Data is invalid.")
            else:
                self.close()
                self.main_window.show_login_window()


    def onlogin(self, event):
        self.close()
        self.main_window.show_login_window()
