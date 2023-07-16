from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QWidget
from websockets.sync.client import connect
import json

from ui.lobby import Ui_LobbyWindow


class WsWaitThread(QThread):
    """
    PyQt thread for waiting websocket data on the game begin.
    Sends signal to the main window to start game.
    """
    finished = pyqtSignal(dict)

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def run(self):
        with connect(
                f"ws://{self.main_window.config['server_address']}{self.main_window.config['wait_player_url']}"
        ) as ws:
            ws.send(self.main_window.config['user']['username'])
            data = ws.recv()
            self.finished.emit(json.loads(data))


class LobbyWindow(QWidget):

    def __init__(self, parent):
        self.main_window = parent
        super().__init__(parent)
        self.ui = Ui_LobbyWindow()
        self.is_waiting_for_players = False

    def setup(self):
        self.ui.setupUi(self.main_window)
        self.ui.start_self_game_button.clicked.connect(self.on_start_self_game)
        self.ui.join_game_button.clicked.connect(self.on_join_game)

    def on_start_self_game(self, event):
        return self.main_window.show_chessboard_self_window()

    def on_join_game(self, event):
        if not self.is_waiting_for_players:
            self.is_waiting_for_players = True
            self.wait_for_players()
        else:
            self.is_waiting_for_players = False

    def wait_for_players(self) -> None:
        self.thread = WsWaitThread(self)
        self.thread.finished.connect(self.main_window.show_chessboard_window)
        self.thread.start()
