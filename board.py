import itertools
from typing import List, Tuple, Optional, Iterable
import pygame
from piece import Piece, PieceColor, PieceType

class ChessBoard:
    def __init__(self) -> None:
        self._board = [[None for _ in range(8)] for _ in range(8)]
        self._moves = []
        self._captured = {"WHITE": [], "BLACK": []}
        
    def __str__(self) -> str:
        retStr = "  a b c d e f g h\n"
        for row in range(8):
            retStr += f"{str(row + 1)}"
            rowStr = ""
            for col in range(8):
                rowStr = " ".join([rowStr, str(self._board[row][col]) if self._board[row][col] is not None else "."])
            retStr += rowStr + "\n"
        retStr += "  a b c d e f g h"
        return retStr
    
    def __repr__(self) -> str:
        return "\n".join(["".join([repr(self._board[y][x]) if self._board[y][x] is not None else " " for x in range(8)]) for y in range(8)])
    
    def __getitem__(self, key: Tuple[str, int]) -> Optional[Piece]:
        row = key[1]-1
        col = ord(key[0].lower()) - ord('a')
        return self._board[row][col]
    
    def __setitem__(self, key: Tuple[str, int], value: Piece) -> None:
        row = key[1]-1
        col = ord(key[0].lower()) - ord('a')
        self._board[row][col] = value
        
    def __iter__(self) -> Iterable[Piece]:
        for row in self._board:
            for piece in row:
                if piece is not None:
                    yield piece
    
    @property
    def board(self) -> List[List[Optional[Piece]]]:
        """
        Returns the board.
        """
        return self._board
    
    @property
    def moves(self) -> List[Tuple[str, int]]:
        """
        Returns the moves.
        """
        return self._moves
    
    @moves.setter
    def moves(self, newMoves: List[Tuple[str, int]]) -> None:
        self._moves = newMoves
        
    @property
    def captured(self) -> List[Piece]:
        """
        Returns the captured pieces.
        """
        return self._captured
    
    @captured.setter
    def captured(self, newCaptured: List[Piece]) -> None:
        self._captured = newCaptured
    
    def isEmpty(self, position: Tuple[str, int]) -> bool:
        """
        Returns True if the position is empty.
        """
        return self[position] is None
    
    def isOccupied(self, position: Tuple[str, int]) -> bool:
        """
        Returns True if the position is occupied.
        """
        return self[position] is not None

    def isValidPosition(self, position: Tuple[str, int]) -> bool:
        """
        Returns True if the position is valid.
        """
        row = position[1]
        col = ord(position[0].lower()) - ord('a')
        return 0 <= row <= 7 and 0 <= col <= 7
    
    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the board.
        """
        for row, col in itertools.product(range(8), range(8)):
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, (195, 160, 130), ((7 - col) * 100, row * 100, 100, 100))
            else:
                pygame.draw.rect(screen, (242, 225, 195), ((7 - col) * 100, row * 100, 100, 100))
        for piece in self:
            if piece is not None:
                piece.draw(screen)
                    
    def getPieces(self, color: PieceColor) -> List[Piece]:
        """
        Returns the pieces of the given color.
        """
        return [piece for piece in self if piece.pieceColor == color]
    
    def toFEN(self) -> str:
        """
        Returns the FEN representation of the board.
        """
        fen = ""
        for row in range(8):
            empty = 0
            for col in range(8):
                if self._board[row][col] is None:
                    empty += 1
                else:
                    if empty != 0:
                        fen += str(empty)
                        empty = 0
                    fen += repr(self._board[row][col])
            if empty != 0:
                fen += str(empty)
            if row != 7:
                fen += "/"
        return fen
    
    def _toSpaces(self, fen: str) -> str:
        """
        Converts the FEN representation to spaces.
        """
        return "".join(" " * int(char) if char.isdigit() else char for char in fen)
    
    # TODO: Fix this
    def fromFEN(self, fen: str) -> None:
        """
        Sets the board to the given FEN representation.
        """
        self.reset()
        rows = self._toSpaces(fen).split("/")
        for row, col in itertools.product(range(8), range(8)):
            if rows[row][col] != " ":
                col = chr(ord('a') + col)
                print(row, col)
                self._board[row][col] = self._fenCharToPiece(rows[col][row], (col, row))
                print(self._board[row][col])
        self._moves = []
        self._captured = {"WHITE": [], "BLACK": []}
        
    def _fenCharToPiece(self, fenChar: str, position: Tuple[str, int]) -> Optional[Piece]:
        if fenChar.isupper():
            match fenChar:
                case "P":
                    return Piece(PieceType.PAWN, PieceColor.WHITE, position)
                case "R":
                    return Piece(PieceType.ROOK, PieceColor.WHITE, position)
                case "N":
                    return Piece(PieceType.KNIGHT, PieceColor.WHITE, position)
                case "B":
                    return Piece(PieceType.BISHOP, PieceColor.WHITE, position)
                case "Q":
                    return Piece(PieceType.QUEEN, PieceColor.WHITE, position)
                case "K":
                    return Piece(PieceType.KING, PieceColor.WHITE, position)
        else:
            match fenChar:
                case "p":
                    return Piece(PieceType.PAWN, PieceColor.BLACK, position)
                case "r":
                    return Piece(PieceType.ROOK, PieceColor.BLACK, position)
                case "n":
                    return Piece(PieceType.KNIGHT, PieceColor.BLACK, position)
                case "b":
                    return Piece(PieceType.BISHOP, PieceColor.BLACK, position)
                case "q":
                    return Piece(PieceType.QUEEN, PieceColor.BLACK, position)
                case "k":
                    return Piece(PieceType.KING, PieceColor.BLACK, position)
    
    def reset(self) -> None:
        """
        Resets the board.
        """
        self._board = [[None for _ in range(8)] for _ in range(8)]
        self._moves = []
        self._captured = {"WHITE": [], "BLACK": []}