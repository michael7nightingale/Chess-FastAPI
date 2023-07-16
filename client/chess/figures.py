from .base import Figure, Color

__all__ = ("Pawn", "Tower", "King", "Queen", "Soldier", "Horse", "EmptyFigure", "Figure")


class Pawn(Figure):
    _x_step = 0
    _x_differ = 1

    def __init__(self, data, chessboard, row, column):
        super().__init__(data, chessboard, row, column)
        self._coef = -1 if self.color is Color.black else 1
        self._y_differ = 1 * self._coef
        self._initial_y = 1 if self.color is Color.black else 6
        self._y_step = 1 * self._coef

    def move(self, other: Figure):
        if isinstance(other, EmptyFigure):    # check if fig can be moved to an empty cell
            if self.row == self._initial_y:    # when pawn can move 2 cells
                is_moved = (
                        self - other == (2 * self._coef, self._x_step)
                        or
                        self - other == (self._y_step, self._x_step)
                )
            else:   # usual 1-cell move
                is_moved = self - other == (self._y_step, self._x_step)
            if is_moved:
                self.chessboard.change(other, self)
            return is_moved
        else:
            if other.color is self.color:  # can't cut one-colored
                return False
            else:
                cutted = self - other
                is_cutted = (abs(cutted[1]) == self._x_differ) and (cutted[0] == self._y_differ)
                if is_cutted:
                    self.chessboard.replace(other, self)
                return is_cutted

    def get_all_moves(self):
        pass


class EmptyFigure(Figure):
    def __init__(self, data, chessboard, row, column):
        super().__init__(data, chessboard, row, column)
        self.color = None

    def move(self, other: Figure):
        return False

    def get_all_moves(self):
        return ()


class King(Figure):
    _x_step = 1
    _y_step = 1
    _x_differ = 1
    _y_differ = 1

    def change_with_tower(self, tower: Figure):
        pass

    def move(self, other: Figure):
        if isinstance(other, Tower) and other.color == self.color:
            return self.change_with_tower(other)
        
        if self.color == other.color:
            return False

        cutted = self - other
        if sorted(map(abs, cutted)) in ([0, 1], [1, 1]):
            return True

    def get_all_moves(self):
        pass


class Soldier(Figure):

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


def match(char: str, *args, **kwargs) -> Figure | None:
    """Return initialized figure object on given char."""
    if char == '':
        return EmptyFigure(data=char, *args, **kwargs)
    elif char in ('♖', '♜'):
        return Tower(data=char, *args, **kwargs)
    elif char in ('♙', '♟'):
        return Pawn(data=char, *args, **kwargs)
    elif char in ('♛', '♕'):
        return Queen(data=char, *args, **kwargs)
    elif char in ('♚', '♔'):
        return King(data=char, *args, **kwargs)
    elif char in ('♗', '♝'):
        return Soldier(data=char, *args, **kwargs)
    elif char in ('♞', '♘'):
        return Horse(data=char, *args, **kwargs)
    else:
        return None


