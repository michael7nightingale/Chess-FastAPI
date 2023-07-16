from PyQt6.QtWidgets import QMainWindow, QApplication

from requestor import Requestor
from . import LobbyWindow, RegistrationWindow, ChessboardSelfWindow, LoginWindow, ChessboardWindow
from ui.main import Ui_MainWindow
from config import Config


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
        self.lobby_window = LobbyWindow(self, self.config)
        self.chessboard_self_window = ChessboardSelfWindow(self, self.config)

        # on-open-application events to check system state
        self.requestor = Requestor(check_token_func=self.check_token, main_window=self)
        self.check_token()

    def setup(self):
        self.ui.setupUi(self)

    def check_token(self) -> None:
        """Checks if there is token saved in the config."""
        if "token" not in self.config:
            self.show_login_window()
        else:
            self.show_lobby_window()
            self.show()

    def closeEvent(self, event) -> None:
        """Self close event."""
        for window in QApplication.topLevelWidgets():
            window.destroy()

    def show_login_window(self) -> None:
        """Show login window."""
        if not self.login_window.isVisible():
            self.login_window.show()

    def show_registration_window(self) -> None:
        """Show registration window."""
        self.requestor.check_connection()
        if not self.registration_window.isVisible():
            self.registration_window.show()

    def show_lobby_window(self) -> None:
        self.lobby_window.setup()

    def show_chessboard_window(self, data: dict) -> None:
        self.requestor.check_connection()
        self.chessboard_window = ChessboardWindow(parent=self, config=self.config, data=data)
        self.chessboard_window.startGame()

    def show_chessboard_self_window(self) -> None:
        self.chessboard_self_window.setup()
