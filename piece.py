from enum import Enum
from typing import List, Tuple
import pygame




class PieceType(Enum):
    PAWN = 1
    ROOK = 2
    KNIGHT = 3
    BISHOP = 4
    QUEEN = 5
    KING = 6
    

class PieceColor(Enum):
    WHITE = 1
    BLACK = 2


class Piece:
    def __init__(self, pieceType: PieceType, pieceColor: PieceColor, piecePosition: Tuple[str, int]) -> None:
        if not isinstance(pieceType, PieceType):
            raise TypeError("pieceType must be a PieceType.")
        if not isinstance(pieceColor, PieceColor):
            raise TypeError("pieceColor must be a PieceColor.")
        if not isinstance(piecePosition, tuple):
            raise TypeError("piecePosition must be a tuple.")
        if len(piecePosition) != 2:
            raise ValueError("piecePosition must be a tuple of length 2.")
        if not isinstance(piecePosition[0], str):
            raise TypeError("piecePosition[0] must be a string.")
        if not isinstance(piecePosition[1], int):
            raise TypeError("piecePosition[1] must be an int.") 
        self._pieceType = pieceType
        self._pieceColor = pieceColor
        self._piecePosition = piecePosition
        self._pieceMoves = [piecePosition]
        self._isSelected = False
        self._isMoved = False
        self._isChecked = False
        self._isCaptured = False
        self._isDraging = False
        self._image = self._getImage()
        self._image = pygame.transform.scale(self._image, (100, 100))
    
    def __str__(self) -> str:
        return f"{self._pieceColor.name} {self._pieceType.name}"
    
    def __repr__(self) -> str:
        if self._pieceColor == PieceColor.WHITE:
            return "N" if self._pieceType == PieceType.KNIGHT else self._pieceType.name[0].upper()
        else:
            return "n" if self._pieceType == PieceType.KNIGHT else self._pieceType.name[0].lower()
        
    def _getImage(self):
        if self._pieceType == PieceType.PAWN:
            if self._pieceColor == PieceColor.WHITE:
                return pygame.image.load("pieces/white/pawn.png")
            else:
                return pygame.image.load("pieces/black/pawn.png")
        elif self._pieceType == PieceType.ROOK:
            if self._pieceColor == PieceColor.WHITE:
                return pygame.image.load("pieces/white/rook.png")
            else:
                return pygame.image.load("pieces/black/rook.png")
        elif self._pieceType == PieceType.KNIGHT:
            if self._pieceColor == PieceColor.WHITE:
                return pygame.image.load("pieces/white/knight.png")
            else:
                return pygame.image.load("pieces/black/knight.png")
        elif self._pieceType == PieceType.BISHOP:
            if self._pieceColor == PieceColor.WHITE:
                return pygame.image.load("pieces/white/bishop.png")
            else:
                return pygame.image.load("pieces/black/bishop.png")
        elif self._pieceType == PieceType.QUEEN:
            if self._pieceColor == PieceColor.WHITE:
                return pygame.image.load("pieces/white/queen.png")
            else:
                return pygame.image.load("pieces/black/queen.png")
        elif self._pieceType == PieceType.KING:
            if self._pieceColor == PieceColor.WHITE:
                return pygame.image.load("pieces/white/king.png")
            else:
                return pygame.image.load("pieces/black/king.png")
            
    @property
    def pieceType(self) -> PieceType:
        """
        Returns the piece type.
        """
        return self._pieceType
    
    @property
    def pieceColor(self) -> PieceColor:
        """
        Returns the piece color.
        """
        return self._pieceColor
        
    @property
    def piecePosition(self) -> Tuple[str, int]:
        """
        Returns the position of the piece.
        """
        return self._piecePosition
    
    @piecePosition.setter
    def piecePosition(self, newPosition: Tuple[str, int]) -> None:
        self._piecePosition = newPosition
        
    @property
    def pieceMoves(self) -> List[Tuple[str, int]]:
        """
        Returns the list of moves the piece has made.
        """
        return self._pieceMoves
    
    @pieceMoves.setter
    def pieceMoves(self, newMoves: List[Tuple[str, int]]) -> None:
        self._pieceMoves = newMoves
        
    @property
    def isSelected(self) -> bool:
        """
        Returns whether the piece is selected or not.
        """
        return self._isSelected

    @property
    def isMoved(self) -> bool:
        """
        Returns whether the piece has moved or not.
        """
        return self._isMoved
    
    @isMoved.setter
    def isMoved(self, newMoved: bool) -> None:
        self._isMoved = newMoved
        self._isMoved = newMoved
        
    @property
    def isChecked(self) -> bool:
        """
        Returns whether the piece is checked or not.
        """
        return self._isChecked
    
    @isChecked.setter
    def isChecked(self, newChecked: bool) -> None:
        self._isChecked = newChecked
        
    @property
    def isCaptured(self) -> bool:
        """
        Returns whether the piece has been captured or not.
        """
        return self._isCaptured
    
    @isCaptured.setter
    def isCaptured(self, newCaptured: bool) -> None:
        self._isCaptured = newCaptured
        
    @property
    def isDraging(self) -> bool:
        """
        Returns whether the piece is being dragged or not.
        """
        return self._isDraging
    
    @isDraging.setter
    def isDraging(self, newDraging: bool) -> None:
        self._isDraging = newDraging
        
    def move(self, newPosition: Tuple[str, int]) -> None:
        """Moves the piece to the new position.

        Args:
            newPosition (Tuple[str, int]): The new position of the piece. Example: ("A", 2)

        Raises:
            ValueError: If the new position is not on the board.
        """
        row = newPosition[1] - 1
        col = ord(newPosition[0].lower()) - ord('a')
        if row < 0 or row > 7 or col < 0 or col > 7:
            raise ValueError("Invalid move.")
        self._piecePosition = newPosition
        self._isMoved = True
        self.pieceMoves.append(newPosition)
    
    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the piece on the screen.
        """
        screenY = 700 - (self._piecePosition[1] - 1) * 100
        screenX = ((ord(self._piecePosition[0].lower()) - ord('a')) * 100)
        if self.isDraging:
            return
        if self.isSelected:
            pygame.draw.rect(screen, (0, 0, 255), (screenX, screenY, 100, 100), 2)
        screen.blit(self._image, (screenX, screenY))
        
    def drawPrevious(self, screen: pygame.Surface) -> None:
        """
        Draws the previous position of the piece on the screen.
        """
        previousPosition = self.pieceMoves[-2]
        col = ord(previousPosition[0].lower()) - ord('a')
        row = previousPosition[1] - 1
        s = pygame.Surface((100, 100))
        s.set_alpha(128)
        s.fill((255, 255, 0))
        screen.blit(s, (col * 100, 700 - row * 100))
        
    def drag(self, screen: pygame.Surface, mousePosition: Tuple[int, int]) -> None:
        """
        Draws the piece on the screen while dragging.
        """
        screenY = mousePosition[1] - self._image.get_rect().height / 2
        screenX = mousePosition[0] - self._image.get_rect().width / 2
        screen.blit(self._image, (screenX, screenY))
        
    def select(self) -> None:
        """
        Selects the piece.
        """
        self._isSelected = True
        
    def deselect(self) -> None:
        """
        Deselects the piece.
        """
        self._isSelected = False