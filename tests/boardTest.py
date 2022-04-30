import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from board import ChessBoard

def test_ChessBoard_init():
    """
    Tests the ChessBoard class' init method.
    """
    board = ChessBoard()
    assert board.board == [[None for _ in range(8)] for _ in range(8)]
    assert board.moves == []
    assert board.captured == []
    
def test_ChessBoard_str():
    """
    Tests the ChessBoard class' __str__ method.
    """
    board = ChessBoard()
    assert str(board) == """  a b c d e f g h
                            1 . . . . . . . .
                            2 . . . . . . . .
                            3 . . . . . . . .
                            4 . . . . . . . .
                            5 . . . . . . . .
                            6 . . . . . . . .
                            7 . . . . . . . .
                            8 . . . . . . . .
                            """
