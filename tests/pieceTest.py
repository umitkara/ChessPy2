import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piece import Piece, PieceType, PieceColor

def test_Piece_init():
    """
    Tests the Piece class' init method.
    """
    pawn = Piece(PieceType.PAWN, PieceColor.WHITE, ("A", 2))
    assert pawn.pieceType == PieceType.PAWN
    assert pawn.pieceColor == PieceColor.WHITE
    assert pawn.piecePosition == ("A", 2)
    assert pawn.pieceMoves == []
    assert pawn.isSelected == False
    assert pawn.isMoved == False
    assert pawn.isChecked == False
    assert pawn.isCaptured == False
    
def test_Piece_str():
    """
    Tests the Piece class' __str__ method.
    """
    pawn = Piece(PieceType.PAWN, PieceColor.WHITE, ("A", 2))
    assert str(pawn) == "WHITE PAWN"
    
def test_Piece_repr():
    """
    Tests the Piece class' __repr__ method.
    """
    pawn = Piece(PieceType.PAWN, PieceColor.WHITE, ("A", 2))
    assert repr(pawn) == "P"
    
def test_Piece_move():
    """
    Tests the Piece class' move method.
    """
    pawn = Piece(PieceType.PAWN, PieceColor.WHITE, ("A", 2))
    pawn.move(("A", 4))
    assert pawn.piecePosition == ("A", 4)
    assert pawn.isMoved == True
    
def test_Piece_select():
    """
    Tests the Piece class' select method.
    """
    pawn = Piece(PieceType.PAWN, PieceColor.WHITE, ("A", 2))
    pawn.select()
    assert pawn.isSelected == True
    
def test_Piece_deselect():
    """
    Tests the Piece class' deselect method.
    """
    pawn = Piece(PieceType.PAWN, PieceColor.WHITE, ("A", 2))
    pawn.deselect()
    assert pawn.isSelected == False