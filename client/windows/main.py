from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QDialog, QPushButton,
    QVBoxLayout, QLabel,

)
import json
import requests
from collections import UserDict

from ui.main import Ui_MainWindow
from .login import LoginWindow


class Config(UserDict):
    @classmethod
    def load_config(cls):
        with open("config.json") as config_json_file:
            config = json.load(config_json_file)
            return cls(config)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        with open("config.json", "w") as config_json_file:
            json.dump(dict(self.items()), config_json_file)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.config: Config = Config.load_config()
        self.login_window = LoginWindow(self, config=self.config)
        self.login_window.closeEvent = self.closeEventLoginWindow

        self.register_window = object()
        self.check_connection()
        self.check_token()

    def check_connection(self):
        try:
            response = requests.get("http://example.com")
            assert response.status_code == 200
        except Exception:
            self.show_exit_dialog("Bad internet connection")

    def check_token(self):
        # try login or register after check internet connection
        if "token" not in self.config:
            self.show_login_window()

    def show_exit_dialog(self, label):
        dialog = QDialog(self)
        v_layout = QVBoxLayout()
        dialog.setLayout(v_layout)
        text = QLabel(dialog)
        text.setText(label)
        v_layout.addWidget(text)
        accept_button = QPushButton(self)
        accept_button.setText("OK")
        accept_button.clicked.connect(lambda: self.close())
        v_layout.addWidget(accept_button)
        dialog.show()

    def show_login_window(self):
        if not self.login_window.isVisible():
            self.login_window.show()

    def closeEvent(self, event):
        for window in QApplication.topLevelWidgets():
            window.destroy()

    def closeEventLoginWindow(self, event):
        self.login_window = LoginWindow()
        self.login_window.closeEvent = self.closeEventLoginWindow
        self.check_token()
