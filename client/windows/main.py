from PyQt6.QtWidgets import QMainWindow, QApplication

from websockets.sync.client import connect
import asyncio

from requestor import Requestor
from . import LobbyWindow, RegistrationWindow, ChessboardWindow, LoginWindow
from ui.main import Ui_MainWindow
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
        self.lobby_window = LobbyWindow(self, self.config)
        self.chessboard_window = ChessboardWindow(self, self.config)

        # on-open-application events to check system state
        self.requestor = Requestor(check_token_func=self.check_token(), main_window=self)
        self.requestor.check_connection()
        self.wait_for_players()
        self.check_token()

    def wait_for_players(self):
        with connect("ws://localhost:8000/ws/wait-player") as ws:
            ws.send(self.config['user']['username'])
            data = ws.recv(10)
            print(data)

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
        if not self.registration_window.isVisible():
            self.registration_window.show()

    def show_lobby_window(self) -> None:
        self.lobby_window.setup()

    def show_chessboard_window(self) -> None:
        # self.setMinimumSize(self.width(), self.height())
        # self.setMaximumSize(self.width(), self.height())
        self.chessboard_window.setup()

    def on_start_self_game(self, event) -> None:
        self.show_chessboard_window()

    def on_join_game(self, event) -> None:
        self.wait_for_players()
        self.show_chessboard_window()
