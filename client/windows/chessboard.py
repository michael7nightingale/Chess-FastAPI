from PyQt6.QtWidgets import QWidget

from ui.chessboard import Ui_ChessboardWindow


class ChessboardWindow(QWidget):
    def __init__(self, parent, config):
        self.main_window = parent
        self.config = config
        super().__init__(parent)
        self.ui = Ui_ChessboardWindow()

    def setup(self):
        self.ui.setupUi(self.main_window)

    def click_figure(self, event):
        print(event)
