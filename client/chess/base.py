from abc import ABC, abstractmethod
from enum import StrEnum, auto


class Color(StrEnum):
    black = auto()
    white = auto()


class Axis(StrEnum):
    x = auto()
    y = auto()


LETTERS = "abcdefgh"
NUMBERS = "87654321"


CHESSBOARD = (
    ('♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖'),
    ('♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'),
    ("", "", "", "", "", "", "", ""),
    ("", "", "", "", "", "", "", ""),
    ("", "", "", "", "", "", "", ""),
    ("", "", "", "", "", "", "", ""),
    ('♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'),
    ('♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'),
)

BLACK_FIGURES = ('♖', '♔', '♗', '♙', '♘', '♕')
WHITE_FIGURES = ('♛', '♜', '♚',  '♝', '♞', '♟')


class Figure(ABC):

    def __init__(self, data: str,
                 chess,
                 chessboard,
                 row: int,
                 column: int):
        self.chess = chess
        self.chessboard = chessboard
        self.color = Color.black if data in BLACK_FIGURES else Color.white
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
    def get_all_moves(self):
        pass

    def __sub__(self, other):
        return self.row - other.row, self.column - other.column
