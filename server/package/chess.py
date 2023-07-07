import itertools
from abc import ABC, abstractmethod
from .htmlRedactor import generate_chessboard
from enum import StrEnum, auto
from itertools import cycle


class Color(StrEnum):
    black = auto()
    white = auto()


class Axis(StrEnum):
    x = auto()
    y = auto()


class Chess:
    ABC: str = 'abcdefgh'

    def __init__(self, chessboard_=generate_chessboard()):
        self.cut_1 = []
        self.cut_2 = []
        self.access_queue = cycle((Color.white, Color.black))
        self.access_color = next(self.access_queue)
        self.chessboard = chessboard_
        self.last_activated: Figure | None = None
        self.init_figures()

    def init_figures(self):
        for i in range(8):
            for j in range(8):
                data = self.chessboard[i][j]
                if data == '':
                    self.chessboard[i][j] = EmptyFigure(
                            data=data, row=i, column=j, chessboard_=self
                        )
                elif data in ('♖', '♜'):
                    self.chessboard[i][j] = Tower(
                        data=data, row=i, column=j, chessboard_=self
                    )
                elif data in ('♙', '♟'):
                    self.chessboard[i][j] = Pawn(
                        data=data, row=i, column=j, chessboard_=self
                    )
                elif data in ('♛', '♕'):
                    self.chessboard[i][j] = Queen(
                        data=data, row=i, column=j, chessboard_=self
                    )
                elif data in ('♚', '♔'):
                    self.chessboard[i][j] = King(
                        data=data, row=i, column=j, chessboard_=self
                    )
                elif data in ('♗', '♝'):
                    self.chessboard[i][j] = Soldier(
                        data=data, row=i, column=j, chessboard_=self
                    )
                elif data in ('♞', '♘'):
                    self.chessboard[i][j] = Horse(
                        data=data, row=i, column=j, chessboard_=self
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

    def get_figure(self, id_: str):
        row_idx, column_idx = self.id_to_idx(id_)
        return self.chessboard[row_idx][column_idx]

    @classmethod
    def id_to_idx(cls, id_: str) -> tuple[int, int]:
        letter, number = id_
        column_idx = cls.ABC.index(letter)
        row_idx = 8 - int(number)
        return row_idx, column_idx

    @classmethod
    def idx_to_id(cls, row: int, column: int) -> str:
        return f"{cls.ABC[column]}{8 - row}"

    def deactivate_all(self):
        for i in self:
            i.active = False
        self.last_activated = None

    def move(self, cell_id: str):
        figure = self.get_figure(cell_id)
        print("Figure in the clicked cell:",  figure)
        print("Last activated: ", self.last_activated)
        if self.last_activated is None:
            color_match = self.access_color == figure.color
        else:
            color_match = self.last_activated.color == self.access_color
            print(19, figure.color)
        if color_match:
            if self.last_activated is None:
                if not isinstance(figure, EmptyFigure):
                    print("None activated")
                    self.deactivate_all()
                    figure.active = True
                    self.last_activated = figure
            else:
                if figure == self.last_activated:
                    print("Clicked and last are the same")
                    self.deactivate_all()
                else:
                    print("Trying to move")
                    to_move = self.last_activated.move(figure)
                    print("Decided to move: ", to_move)
                    if to_move:
                        from_id = self.idx_to_id(*self.last_activated.coords)
                        self.last_activated.coords = figure.coords
                        self.deactivate_all()
                        self.access_color = next(self.access_queue)
                        return from_id
                    else:
                        self.deactivate_all()
                        return

    def replace(self, to_replace, replace_with):
        self.chessboard[replace_with.row][replace_with.column] = EmptyFigure(
            data='', row=replace_with.row, chessboard_=self, column=replace_with.column
        )
        self.chessboard[to_replace.row][to_replace.column] = replace_with

    def change(self, to_change, change_with):
        self.chessboard[change_with.row][change_with.column], self.chessboard[to_change.row][to_change.column] =\
            self.chessboard[to_change.row][to_change.column], self.chessboard[change_with.row][change_with.column]

    def inspect_line(self,
                     begin: tuple[int, int],
                     to: tuple[int, int]) -> bool:
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

    def inspect_diagonal(self,
                         begin: tuple[int, int],
                         to: tuple[int, int]) -> bool:
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


class Figure(ABC):
    figures: dict = {
        "black": ('♖', '♔', '♗', '♙', '♘', '♕'),
        "white": ('♛', '♜', '♚',  '♝', '♞', '♟')
    }
    # bytes?

    def __init__(self, data: str,
                 chessboard_: Chess,
                 row: int,
                 column: int):
        self.chessboard = chessboard_
        self.color = Color.black if data in self.figures['black'] else Color.white
        self.data = data
        self.column = column
        self.row = row
        self.active = False

    @property
    def coords(self) -> tuple[int, int]:
        return self.row, self.column

    @coords.setter
    def coords(self, new_coords: tuple[int, int]) -> None:
        self.row, self.column = new_coords

    @abstractmethod
    def move(self, other: object):
        pass

    @abstractmethod
    def cut(self, other: object):
        pass

    @abstractmethod
    def get_all_moves(self):
        pass

    def __sub__(self, other):
        return self.row - other.row, self.column - other.column


class Pawn(Figure):
    def __init__(self, data, chessboard_, row, column):
        super().__init__(data, chessboard_, row, column)
        self.__x_differ = 1
        self.__coef = -1 if self.color is Color.black else 1
        self.__y_differ = 1 * self.__coef
        self.__initial_y = 1 if self.color is Color.black else 6
        self.__x_step = 0
        self.__y_step = 1 * self.__coef

    def move(self, other: Figure):
        if isinstance(other, EmptyFigure):    # check if fig can be moved to an empty cell
            if self.row == self.__initial_y:    # when pawn can move 2 cells
                is_moved = self - other == (2 * self.__coef, self.__x_step) or self - other == (self.__y_step, self.__x_step)
            else:   # usual 1-cell move
                is_moved = self - other == (self.__y_step, self.__x_step)
            if is_moved:
                self.chessboard.change(other, self)
            return is_moved
        else:
            return self.cut(other)    # cut

    def cut(self, other: Figure) -> bool:
        """Срубить можно фигуру или нет."""
        if other.color is self.color:   # can't cut one-colored
            return False
        else:
            cutted = self - other
            is_cutted = (abs(cutted[1]) == self.__x_differ) and (cutted[0] == self.__y_differ)
            if is_cutted:
                self.chessboard.replace(other, self)
            return is_cutted

    def get_all_moves(self):
        pass


class EmptyFigure(Figure):
    def __init__(self, data, chessboard_, row, column):
        super().__init__(data, chessboard_, row, column)
        self.color = None

    def cut(self, other: object):
        return False

    def move(self, other: Figure):
        return False

    def get_all_moves(self):
        return ()


class King(Figure):
    def cut(self, other: object):
        pass

    def move(self, other: object):
        pass

    def get_all_moves(self):
        pass


class Soldier(Figure):
    def cut(self, other: object):
        pass

    def move(self, other: Figure) -> bool:
        if self.color is other.color:
            return False
        else:
            cutted = self - other
            is_moved = abs(cutted[0]) == abs(cutted[1])
            if is_moved:
                if not self.chessboard.inspect_diagonal(self.coords, other.coords):
                    return False
                else:
                    self.chessboard.replace(other, self)

            return is_moved

    def get_all_moves(self):
        pass


class Horse(Figure):
    __differs = (1, 2)

    def cut(self, other: Figure) -> bool:
        pass

    def move(self, other: Figure) -> bool:
        if self.color is other.color:
            return False
        else:
            cutted = self - other
            is_moved = sorted([abs(i) for i in cutted]) == list(self.__differs)
            if is_moved:
                self.chessboard.replace(other, self)
            return is_moved

    def get_all_moves(self):
        pass


class Tower(Figure):
    def cut(self, other: Figure):
        pass

    def move(self, other: Figure):
        to_move = False
        if self.color is other:
            return False
        else:
            if not all(self - other):
                to_move = self.chessboard.inspect_line(self.coords, other.coords)
            else:
                return False
            if to_move:
                self.chessboard.replace(other, self)
            return to_move

    def get_all_moves(self):
        pass


class Queen(Figure):
    def cut(self, other: object):
        pass

    def move(self, other: Figure) -> bool:
        if self.color is other.color:
            return False
        else:
            cutted = self - other
            to_moved = False
            if not all(cutted):
                to_moved = self.chessboard.inspect_line(self.coords, other.coords)
            elif abs(cutted[0]) == abs(cutted[1]):
                to_moved = self.chessboard.inspect_diagonal(self.coords, other.coords)
            if to_moved:
                self.chessboard.replace(other, self)
            return to_moved

    def get_all_moves(self):
        pass
