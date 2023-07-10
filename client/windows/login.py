from PyQt6.QtWidgets import QWidget
from typing import Mapping

from ui.login import Ui_LoginWindow
from validators import validate_password, validate_username
from qt_tools import alert


class LoginWindow(QWidget):
    def __init__(self, parent, config: Mapping):
        self.main_window = parent
        self.config = config
        super().__init__(parent=None)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.submit_button.clicked.connect(self.onsubmit)
        self.ui.registration_button.clicked.connect(self.on_registration)
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
            response = self.main_window.requestor.post_unauthorized(
                url=self.config['base_url'] + "auth/token",
                json=data,
                window=self
            )
            self.config['token'] = response.json()["access_token"]

            user_data_response = self.main_window.requestor.get_authorized(
                url=self.config['base_url'] + "auth/me",
            )
            self.config['user'] = user_data_response.json()


            self.close()
            self.main_window.show_lobby_window()

    def on_registration(self, event):
        self.close()
        self.main_window.show_registration_window()
