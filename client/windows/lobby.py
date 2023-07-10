from PyQt6.QtWidgets import QWidget
from typing import Mapping

from ui.lobby import Ui_LobbyWindow


class LobbyWindow(QWidget):

    def __init__(self, parent, config: Mapping):
        self.main_window = parent
        self.config = config
        super().__init__(parent)
        self.ui = Ui_LobbyWindow()

    def setup(self):
        self.ui.setupUi(self.main_window)
        self.ui.start_self_game_button.clicked.connect(self.main_window.on_start_self_game)
        self.ui.join_game_button.clicked.connect(self.main_window.on_join_game)

