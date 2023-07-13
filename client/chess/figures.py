from .base import Figure, Color

__all__ = ("Pawn", "Tower", "King", "Queen", "Soldier", "Horse", "EmptyFigure", "Figure")


class Pawn(Figure):
    def __init__(self, data, chessboard, row, column):
        super().__init__(data, chessboard, row, column)
        self.__x_differ = 1
        self.__coef = -1 if self.color is Color.black else 1
        self.__y_differ = 1 * self.__coef
        self.__initial_y = 1 if self.color is Color.black else 6
        self.__x_step = 0
        self.__y_step = 1 * self.__coef

    def move(self, other: Figure):
        if isinstance(other, EmptyFigure):    # check if fig can be moved to an empty cell
            if self.row == self.__initial_y:    # when pawn can move 2 cells
                is_moved = (
                    self - other == (2 * self.__coef, self.__x_step)
                    or
                    self - other == (self.__y_step, self.__x_step)
                )
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
    def __init__(self, data, chessboard, row, column):
        super().__init__(data, chessboard, row, column)
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
