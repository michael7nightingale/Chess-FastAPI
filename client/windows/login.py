from PyQt6.QtWidgets import QWidget
import requests
from typing import Mapping

from ui.login import Ui_LoginWindow
from validators import validate_password, validate_username
from qt_tools import alert, show_exit_dialog


class LoginWindow(QWidget):
    def __init__(self, parent, config: Mapping):
        self.main_window = parent
        self.config = config
        super().__init__(parent=None)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.submit_button.clicked.connect(self.onsubmit)
        self.ui.registration_button.clicked.connect(self.onregistration)
        self.hide_labels()

    def hide_labels(self):
        """Hide all input labels."""
        self.ui.password_label.hide()
        self.ui.username_label.hide()

    def onsubmit(self, event):
        self.hide_labels()
        were_alerts = False
        # check username
        username = self.ui.username_input.text()
        if not validate_username(username):
            were_alerts = True
            alert(self.ui.username_label, "Username is invalid.")
        # check password
        password = self.ui.password_input.text()
        if not validate_password(password):
            were_alerts = True
            alert(self.ui.password_label, "Password is invalid.")

        if not were_alerts:
            # try to send request
            data = {
                "username": username,
                "password": password
            }
            try:
                response = requests.post(
                    url=self.config['base_url'] + "auth/token",
                    json=data
                )
                assert response.status_code == 200
                self.config['token'] = response.json()['access_token']
            except requests.ConnectionError:
                show_exit_dialog(self, "Cannot connect to the server.")
            except AssertionError:
                show_exit_dialog(self, "User has not been found.")
            else:
                self.close()
                self.main_window.check_token()

    def onregistration(self, event):
        self.close()
        self.main_window.show_registration_window()
