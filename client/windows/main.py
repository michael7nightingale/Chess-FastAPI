from PyQt6.QtWidgets import QMainWindow, QApplication
import requests

from ui.main import Ui_MainWindow
from .login import LoginWindow
from .registration import RegistrationWindow
from config import Config
from qt_tools import show_exit_dialog


class MainWindow(QMainWindow):
    """
    Qt main window for application att all.
    """
    def __init__(self):
        super().__init__(parent=None)
        # setup main window ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # configuration
        self.config: Config = Config.load_config()

        # setup subwindows
        self.login_window = LoginWindow(self, self.config)
        self.registration_window = RegistrationWindow(self, self.config)

        # on-open-application events to check system state
        self.check_connection()
        self.check_token()

    def check_connection(self):
        """Check connection to the internet."""
        try:
            response = requests.get("https://example.com")
            assert response.status_code == 200
        except Exception:
            show_exit_dialog(self, "Bad internet connection")

    def check_token(self):
        """Checks if there is token saved in the config."""
        if "token" not in self.config:
            self.show_login_window()
        else:
            self.show()

    def closeEvent(self, event):
        """Self close event."""
        for window in QApplication.topLevelWidgets():
            window.destroy()

    def show_login_window(self):
        """Show login window."""
        if not self.login_window.isVisible():
            self.login_window.show()

    def show_registration_window(self):
        """Show registration window."""
        if not self.registration_window.isVisible():
            self.registration_window.show()
