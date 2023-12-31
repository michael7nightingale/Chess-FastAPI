from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtCore import QThread, pyqtSignal
import json
from websockets.sync.client import ClientConnection, connect

from ui.chessboard import Ui_ChessboardWindow
from chess import CHESSBOARD, NUMBERS, LETTERS
from models import Move
from qt_tools import show_dialog


class WsMaker:
    """
    Very interesting class to generate ws internally in the context manager.
    """
    def __init__(self, url: str):
        self.url = url
        self.sentinel = False
        self.ws_gen = iter(self)

    def close(self):
        self.sentinel = True
        next(self.ws_gen)   # to break iter cycle and close the connection

    def __iter__(self):
        with connect(self.url) as ws:
            while True:
                if self.sentinel:
                    break
                yield ws
            ws.close()

    def __call__(self, *args, **kwargs) -> ClientConnection:
        ws = next(self.ws_gen)
        return ws


class WsChessThread(QThread):
    """
    PyQt thread for receiving ws data and sending signal to the parent window.
    """
    move_signal = pyqtSignal(Move)
    after_game_signal = pyqtSignal(str)

    def __init__(self, parent, ws: WsMaker):
        super().__init__(parent=parent)
        self.ws = ws

    def run(self):
        while True:
            try:
                move_data = self.ws().recv()
                move_data_dict = json.loads(move_data)
                status = move_data_dict['status']
                match status:
                    case 200:
                        move = Move(**move_data_dict)
                        self.move_signal.emit(move)
                    case 303:
                        self.ws.close()
                        return self.after_game_signal.emit(move_data_dict['message'])
                    case 401:
                        return self.after_game_signal.emit(move_data_dict['message'])
            except Exception:
                break


class ChessboardWindow(QWidget):
    def __init__(self, parent, data):
        self.main_window = parent
        super().__init__(parent)
        self.data: dict = data
        self.game_id = self.data['game_id']
        self.ui = Ui_ChessboardWindow()
        game_url = self.main_window.config['game_url'].replace("{game_id}", self.game_id)
        self.ws = WsMaker(
            url=f"ws://{self.main_window.config['server_address']}{game_url}"
        )
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

    def startGame(self) -> None:
        """Start game function."""
        self.setup()
        self.setChessboard()
        self.thread.move_signal.connect(self.process_move)
        self.thread.after_game_signal.connect(self.on_after_game)
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

    def process_move(self, move: Move) -> None:
        """Function that process move of GUI figures."""
        self.move_figure(
            from_id=move.from_id,
            to_id=move.to_id,
            to_data=move.to_data,
            from_data=move.from_data
        )
        self.add_move_to_list(
            from_id=move.from_id,
            to_id=move.to_id,
            user=move.move_user
        )
        self.change_move_color(move.new_color)

    def change_move_color(self, color: str) -> None:
        self.ui.move_color_label.setText(color)

    def move_figure(self, from_id: str, to_id: str, from_data: str, to_data: str) -> None:
        """Function that moves GUI figures."""
        from_cell = self.ui.centralwidget.findChild(QLabel, from_id)
        to_cell = self.ui.centralwidget.findChild(QLabel, to_id)
        if from_data and to_data:
            to_cell.setText(from_data)
            from_cell.setText("")
        else:
            to_cell.setText(from_data)
            from_cell.setText(to_data)

    def add_move_to_list(self, from_id: str, to_id: str, user: str) -> None:
        item = f"{from_id} -> {to_id} ({user})"
        self.ui.moves_list.addItem(item)

    def on_after_game(self, message: str):
        show_dialog(self, message)
        self.main_window.show_lobby_window()
