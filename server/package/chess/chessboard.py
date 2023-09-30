import itertools
from copy import deepcopy
from enum import Enum, auto

from .base import CHESSBOARD, Color, LETTERS
from .figures import EmptyFigure, match, Figure, King


class MoveEnum(Enum):
    """Move signals enum."""
    CHECK = auto()
    CHECK_AND_MATE = auto()
    WALK = auto()
    CUT = auto()


class Chess:
    """
    Chess game class.
    """

    def __init__(self, chessboard=CHESSBOARD):
        self.access_color_queue = itertools.cycle((Color.white, Color.black))
        self.access_color = next(self.access_color_queue)
        self.check: bool = False
        self.check_and_mate: bool = False
        self.white_king = None
        self.black_king = None
        self.chessboard = [list(row) for row in chessboard]
        self.last_activated: Figure | None = None
        self.init_figures()

    @property
    def check_to_color(self):
        if not self.check:
            return None
        return self.access_color

    def is_check(self, target_king: King, chessboard=None):
        # print(f"Check check for {target_king.color} king")
        if chessboard is None:
            chessboard = deepcopy(self.chessboard)

        for row in chessboard:
            for fig in row:
                if not isinstance(fig, EmptyFigure) and fig.color is not target_king.color:
                    to_move = fig.move(target_king, chessboard)
                    if to_move:
                        return True
        return False

    def is_check_and_mate(self):
        if self.access_color == 'access_color':
            pass

    def init_figures(self) -> None:
        """Translate symbols to objects."""
        for i in range(8):
            for j in range(8):
                data = self.chessboard[i][j]
                self.chessboard[i][j] = match(char=data, row=i, column=j, chess=self, chessboard=self.chessboard)
        # set colored king figures
        for fig in self:
            if isinstance(fig, King):
                if fig.color is Color.white:
                    self.white_king = fig
                else:
                    self.black_king = fig

    def change_access_color(self) -> None:
        self.access_color = next(self.access_color_queue)

    @property
    def chessboard(self):
        return self._chessboard

    @property
    def not_access_color(self):
        if self.access_color is Color.white:
            return Color.black
        else:
            return Color.white

    @chessboard.setter
    def chessboard(self, new_value):
        if not hasattr(self, '__chessboard'):
            self._chessboard = new_value
        else:
            raise TypeError("Chessboard cant`t be changed.")

    def __iter__(self):
        return itertools.chain(*self.chessboard)

    def get_figure(self, id_: str) -> Figure:
        """Get figure by its is on the chessboard."""
        row_idx, column_idx = self.id_to_idx(id_)
        return self.chessboard[row_idx][column_idx]

    @classmethod
    def id_to_idx(cls, id_: str) -> tuple[int, int]:
        """Convert cell id to idx."""
        letter, number = id_
        column_idx = LETTERS.index(letter)
        row_idx = 8 - int(number)
        return row_idx, column_idx

    @classmethod
    def idx_to_id(cls, row: int, column: int) -> str:
        """Convert cell idx to id."""
        return f"{LETTERS[column]}{8 - row}"

    def deactivate_all(self) -> None:
        """Set all cells` state to unactivated."""
        for i in self:
            i.active = False
        self.last_activated = None

    def will_be_check(self, to_figure, from_figure, target_king: King) -> bool:
        to_figure_copy = deepcopy(to_figure)
        from_figure_copy = deepcopy(from_figure)

        chessboard: list[list[Figure]] = [[f for f in row] for row in self.chessboard]
        chessboard[from_figure_copy.row][from_figure_copy.column] = EmptyFigure(
            data='',
            row=from_figure_copy.row,
            chess=self,
            chessboard=chessboard,
            column=from_figure_copy.column
        )

        new_figure_coords = to_figure_copy.coords
        from_figure_copy.coords = new_figure_coords
        if isinstance(from_figure_copy, King):
            target_king = from_figure_copy
        chessboard[from_figure_copy.row][from_figure_copy.column] = from_figure_copy
        is_check = self.is_check(target_king, chessboard)
        return is_check

    def move(self, cell_id: str) -> None | tuple[tuple[str, str], tuple[str, str], MoveEnum]:
        """Move figure function."""
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

                    from_id = self.idx_to_id(*self.last_activated.coords)
                    if self.last_activated.color == figure.color:
                        return
                    to_move = self.last_activated.move(figure)
                    if to_move:
                        if self.will_be_check(figure, self.last_activated, self.target_king):
                            print("WILL BE CHECK")
                            return

                        if isinstance(figure, EmptyFigure):
                            self.walk(figure, self.last_activated)
                            move_signal = MoveEnum.WALK
                        else:
                            self.cut(figure, self.last_activated)
                            move_signal = MoveEnum.CUT
                        data = (self.last_activated.data, figure.data)
                        self.deactivate_all()
                        self.change_access_color()
                        # check is there is `check` or `check and mate`
                        if self.is_check(self.target_king):
                            self.check = True
                            print("CHECK!!!")
                            move_signal = MoveEnum.CHECK
                        if self.is_check_and_mate():
                            self.check_and_mate = True
                            move_signal = MoveEnum.CHECK_AND_MATE
                        # send move data
                        return (from_id, cell_id), data, move_signal
                    else:
                        self.deactivate_all()
                        return

    @property
    def target_king(self) -> King:
        return self.black_king if self.access_color is Color.black else self.white_king

    def cut(self, to_cut, from_cut) -> None:
        """Cut a figure."""
        self.chessboard[from_cut.row][from_cut.column] = EmptyFigure(
            data="",
            chess=self,
            chessboard=self.chessboard,
            row=from_cut.row,
            column=from_cut.column
        )
        new_figure_coords = to_cut.coords
        from_cut.coords = new_figure_coords
        self.chessboard[from_cut.row][from_cut.column] = from_cut

    def walk(self, to_walk: EmptyFigure, from_walk: Figure) -> None:
        """Change a figure."""
        new_figure_coords = to_walk.coords
        self.chessboard[from_walk.row][from_walk.column] = EmptyFigure(
            data="",
            chess=self,
            chessboard=self.chessboard,
            row=from_walk.row,
            column=from_walk.column
        )
        from_walk.coords = new_figure_coords
        self.chessboard[to_walk.row][to_walk.column] = from_walk

    @classmethod
    def inspect_line(
            cls,
            chessboard: list[list[Figure]],
            begin: tuple[int, int],
            to: tuple[int, int]
    ) -> bool:
        """
        Function that check if there is busy cell on the given line
        (row, column) by coordinates of the chessboard matrix.
        """
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
            if not isinstance(chessboard[x1][y1], EmptyFigure):
                is_free = False
                break
            x1 += x_step
            y1 += y_step

        return is_free

    @classmethod
    def inspect_diagonal(
            cls,
            chessboard: list[list[Figure]],
            begin: tuple[int, int],
            to: tuple[int, int]
    ) -> bool:
        """
        Function that check if there is busy cell on the given diagonal
        by coordinates  of the chessboard matrix.
        """
        (x1, y1), (x2, y2) = begin, to
        x_step = 1 if x1 < x2 else -1
        y_step = 1 if y1 < y2 else -1
        times = abs(x2 - x1) - 1
        is_free = True
        x1 += x_step
        y1 += y_step
        for _ in range(times):
            if not isinstance(chessboard[x1][y1], EmptyFigure):
                is_free = False
                break
            x1 += x_step
            y1 += y_step
        return is_free
