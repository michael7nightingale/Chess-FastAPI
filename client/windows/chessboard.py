from PyQt6.QtWidgets import QWidget, QLabel
from ui.chessboard import Ui_ChessboardWindow

from chess import Chess, CHESSBOARD, NUMBERS, LETTERS


class ChessboardWindow(QWidget):
    def __init__(self, parent, config, data):
        self.main_window = parent
        self.config = config
        super().__init__(parent)
        self.data: dict = data
        self.ui = Ui_ChessboardWindow()

    def setChessboard(self) -> None:
        """Place all figures on the desk."""
        self.chess = Chess()
        for row, number in enumerate(NUMBERS):
            for column, letter in enumerate(LETTERS):
                cell_name = letter + str(number)
                self.ui.centralwidget.findChild(QLabel, cell_name).setText(
                    CHESSBOARD[row][column]
                )

    def setup(self) -> None:
        """Set up GUI for lobby window inside the main window."""
        self.ui.setupUi(self.main_window)
        self.ui.move_color_label.setText("Белые")
        self.ui.enemy_label.setText(self.data['enemy'])
        self.ui.you_color_label.setText(self.data['you_color'])
        self.setChessboard()

    def click_figure(self, event, cell: QLabel) -> None:
        """Function on clicking the chessboard cell."""
        cell_id = cell.objectName()
        to_move: str | None = self.chess.move(cell_id)
        if to_move is not None:
            (from_id, to_id), (from_data, to_data) = to_move
            from_cell = self.ui.centralwidget.findChild(QLabel, from_id)
            if all((from_data, to_data)):
                cell.setText(from_data)
                from_cell.setText("")
            else:
                cell.setText(from_data)
                from_cell.setText(to_data)
