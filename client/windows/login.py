from PyQt6.QtWidgets import QWidget
import requests

from ui.login import Ui_LoginWindow


def validate_username(username: str):
    if len(username) < 5:
        return False


def validate_password(password):
    if len(password) < 5:
        return False


class LoginWindow(QWidget):
    def __init__(self, parent=None, config: dict = None):
        self.main_window = parent
        self.config = config
        super().__init__(parent=None)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.hide_labels()
        self.ui.pushButton.clicked.connect(self.onclick)

    def hide_labels(self):
        self.ui.password_label.hide()
        self.ui.username_label.hide()

    def alert(self, label, text):
        label.show()
        label.setText(text)

    def onclick(self):
        self.hide_labels()
        username = self.ui.username_input.text()
        if not validate_username(username):
            self.alert(self.ui.username_label, "Username is too short")

        password = self.ui.password_input.text()
        if not validate_password(password):
            self.alert(self.ui.password_label, "Password is too short")

        # try to send request
        data = {
            "username": username,
            "password": password
        }
        try:
            response = requests.post(url=self.config['base_url'] + "auth/token", json=data)
            assert response.status_code == 200
            self.config['token'] = response.json()['access_token']
        except Exception:
            self.main_window.show_exit_dialog("Cannot connect to the server.")

        self.close()



