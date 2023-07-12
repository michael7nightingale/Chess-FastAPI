import itertools
from .base import CHESSBOARD, Color, LETTERS

from .figures import *


class Chess:
    def __init__(self, chessboard=CHESSBOARD):
        self.access_queue = itertools.cycle((Color.white, Color.black))
        self.access_color = next(self.access_queue)
        self.chessboard = [list(row) for row in chessboard]
        self.last_activated: Figure | None = None
        self.init_figures()

    def changeAccessColor(self) -> None:
        self.access_color = next(self.access_queue)

    def init_figures(self) -> None:
        """Translate symbols to objects."""
        for i in range(8):
            for j in range(8):
                data = self.chessboard[i][j]
                if data == '':
                    self.chessboard[i][j] = EmptyFigure(
                            data=data, row=i, column=j, chessboard=self
                        )
                elif data in ('♖', '♜'):
                    self.chessboard[i][j] = Tower(
                        data=data, row=i, column=j, chessboard=self
                    )
                elif data in ('♙', '♟'):
                    self.chessboard[i][j] = Pawn(
                        data=data, row=i, column=j, chessboard=self
                    )
                elif data in ('♛', '♕'):
                    self.chessboard[i][j] = Queen(
                        data=data, row=i, column=j, chessboard=self
                    )
                elif data in ('♚', '♔'):
                    self.chessboard[i][j] = King(
                        data=data, row=i, column=j, chessboard=self
                    )
                elif data in ('♗', '♝'):
                    self.chessboard[i][j] = Soldier(
                        data=data, row=i, column=j, chessboard=self
                    )
                elif data in ('♞', '♘'):
                    self.chessboard[i][j] = Horse(
                        data=data, row=i, column=j, chessboard=self
                    )

    @property
    def chessboard(self):
        return self.__chessboard

    @chessboard.setter
    def chessboard(self, new_value):
        if not hasattr(self, '__chessboard'):
            self.__chessboard = new_value
        else:
            raise TypeError("Chessboard cant`t be changed.")

    def __iter__(self):
        return itertools.chain(*self.chessboard)

    def get_figure(self, id_: str) -> Figure:
        row_idx, column_idx = self.id_to_idx(id_)
        return self.chessboard[row_idx][column_idx]

    @classmethod
    def id_to_idx(cls, id_: str) -> tuple[int, int]:
        letter, number = id_
        column_idx = LETTERS.index(letter)
        row_idx = 8 - int(number)
        return row_idx, column_idx

    @classmethod
    def idx_to_id(cls, row: int, column: int) -> str:
        return f"{LETTERS[column]}{8 - row}"

    def deactivate_all(self) -> None:
        for i in self:
            i.active = False
        self.last_activated = None

    def move_declarative(self, from_id, to_id) -> None:
        to_figure = self.get_figure(to_id)
        from_figure = self.get_figure(from_id)
        from_figure.move(to_figure)
        self.deactivate_all()
        self.changeAccessColor()

    def move(self, cell_id: str):
        figure = self.get_figure(cell_id)
        if self.last_activated is None:
            color_match = self.access_color == figure.color
        else:
            color_match = self.last_activated.color == self.access_color
        if color_match:
            if self.last_activated is None:
                if not isinstance(figure, EmptyFigure):
                    self.deactivate_all()
                    figure.active = True
                    self.last_activated = figure
            else:
                if figure == self.last_activated:
                    self.deactivate_all()
                else:
                    if self.last_activated.color == figure.color:
                        return
                    to_move = self.last_activated.move(figure)
                    if to_move:
                        from_id = self.idx_to_id(*self.last_activated.coords)
                        self.last_activated.coords = figure.coords

                        data = (self.last_activated.data, figure.data)

                        self.deactivate_all()
                        self.changeAccessColor()

                        return (from_id, cell_id), data,
                    else:
                        self.deactivate_all()
                        return

    def replace(self, to_replace, replace_with) -> None:
        self.chessboard[replace_with.row][replace_with.column] = EmptyFigure(
            data='', row=replace_with.row, chessboard=self, column=replace_with.column
        )
        self.chessboard[to_replace.row][to_replace.column] = replace_with

    def change(self, to_change, change_with) -> None:
        self.chessboard[change_with.row][change_with.column], self.chessboard[to_change.row][to_change.column] = (
            self.chessboard[to_change.row][to_change.column], self.chessboard[change_with.row][change_with.column]
        )

    def inspect_line(
            self,
            begin: tuple[int, int],
            to: tuple[int, int]
    ) -> bool:
        (x1, y1), (x2, y2) = begin, to
        x_step = 1 if x1 < x2 else -1
        y_step = 1 if y1 < y2 else -1
        if x1 - x2 == 0:
            x_step = 0
            times = abs(y2 - y1) - 1
        else:
            y_step = 0
            times = abs(x2 - x1) - 1
        is_free = True
        x1 += x_step
        y1 += y_step
        for _ in range(times):
            if not isinstance(self.chessboard[x1][y1], EmptyFigure):
                is_free = False
                break
            x1 += x_step
            y1 += y_step

        return is_free

    def inspect_diagonal(
            self,
            begin: tuple[int, int],
            to: tuple[int, int]
    ) -> bool:
        (x1, y1), (x2, y2) = begin, to
        x_step = 1 if x1 < x2 else -1
        y_step = 1 if y1 < y2 else -1
        times = abs(x2 - x1) - 1
        is_free = True
        x1 += x_step
        y1 += y_step
        for _ in range(times):
            if not isinstance(self.chessboard[x1][y1], EmptyFigure):
                is_free = False
                break
            x1 += x_step
            y1 += y_step
        return is_free
