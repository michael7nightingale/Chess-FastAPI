from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtCore import QThread, pyqtSignal
import json
from websockets.sync.client import ClientConnection, connect

from ui.chessboard import Ui_ChessboardWindow
from chess import Chess, CHESSBOARD, NUMBERS, LETTERS


class WsMaker:
    """
    Very interesting class to generate ws internally in the context manager.
    """
    def __init__(self, url: str):
        self.url = url
        self.ws_gen = iter(self)

    def __iter__(self):
        with connect(self.url) as ws:
            while True:
                yield ws

    def __call__(self, *args, **kwargs) -> ClientConnection:
        ws = next(self.ws_gen)
        return ws


class WsChessThread(QThread):
    """
    PyQt thread for receiving ws data and sending signal to the parent window.
    """
    move_signal = pyqtSignal(dict)

    def __init__(self, parent, ws: WsMaker):
        super().__init__(parent=parent)
        self.ws = ws

    def run(self):
        while True:
            move_data = self.ws().recv(1000)
            self.move_signal.emit(json.loads(move_data))


class ChessboardWindow(QWidget):
    def __init__(self, parent, config, data):
        self.main_window = parent
        self.config = config
        super().__init__(parent)
        self.data: dict = data
        self.game_id = self.data['game_id']
        self.ui = Ui_ChessboardWindow()
        self.ws = WsMaker(url=f"ws://localhost:8001/ws/chess/{self.game_id}")
        self.thread = WsChessThread(parent=self, ws=self.ws)

    def setup(self) -> None:
        """Set up GUI for lobby window inside the main window."""
        self.ui.setupUi(self.main_window)
        self.ui.move_color_label.setText("Белые")
        self.ui.enemy_label.setText(self.data['enemy'])
        self.ui.you_color_label.setText(self.data['you_color'])
        self.setChessboard()

    def setChessboard(self) -> None:
        """Place all figures on the desk."""
        for row, number in enumerate(NUMBERS):
            for column, letter in enumerate(LETTERS):
                cell_name = letter + str(number)
                self.ui.centralwidget.findChild(QLabel, cell_name).setText(
                    CHESSBOARD[row][column]
                )

    def startGame(self):
        """Start game function."""
        self.setup()
        self.setChessboard()
        self.thread.move_signal.connect(self.move_figure)
        self.thread.start()

    def click_figure(self, event, cell: QLabel) -> None:
        """Function on clicking the chessboard cell."""
        cell_id = cell.objectName()
        move_data = {
            "cell_id": cell_id,
            "user": self.data['you'],
            "color": self.data['you_color']
        }
        self.ws().send(json.dumps(move_data))

    def move_figure(self, move_data: dict) -> None:
        """Function that moves GUI figures"""
        from_id = move_data['from_id']
        to_id = move_data['to_id']
        from_data = move_data['from_data']
        to_data = move_data['to_data']
        to_cell = self.ui.centralwidget.findChild(QLabel, to_id)
        from_cell = self.ui.centralwidget.findChild(QLabel, from_id)
        if from_data and to_data:
            to_cell.setText(from_data)
            from_cell.setText("")
        else:
            to_cell.setText(from_data)
            from_cell.setText(to_data)
