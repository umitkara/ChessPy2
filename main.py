import pygame
from game import ChessGame
import pathlib
import tkinter as tk
from PIL import Image, ImageTk

from piece import PieceColor

pColor = PieceColor.WHITE
cLevel = 1

class LevelSelection:
    def __init__(self, master=None):
        whitesImage = Image.open(pathlib.Path(__file__).parent.absolute() / "pieces" / "white" / "king.png")
        whitesImage = whitesImage.convert("RGBA")
        whitesImage = whitesImage.resize((100, 100), Image.ANTIALIAS)
        blackImage = Image.open(pathlib.Path(__file__).parent.absolute() / "pieces" / "black" / "king.png")
        blackImage= blackImage.convert("RGBA")
        blackImage= blackImage.resize((100, 100), Image.ANTIALIAS)
        self.frame1 = tk.Frame(master)
        self.selectWhites = tk.Button(self.frame1)
        self.img_king = ImageTk.PhotoImage(whitesImage)
        self.selectWhites.configure(image=self.img_king, command=self.whitesClicked)
        self.selectWhites.grid(column="0", row="0")
        self.selectBlacks = tk.Button(self.frame1)
        self.img_queen = ImageTk.PhotoImage(blackImage)
        self.selectBlacks.configure(image=self.img_queen, command=self.blacksClicked)
        self.selectBlacks.grid(column="1", row="0")
        self.scale1 = tk.Scale(self.frame1)
        self.scale1.configure(bigincrement="1", digits="1", from_="1", label="Level")
        self.scale1.configure(
            orient="horizontal", resolution="0.0", showvalue="true", sliderlength="10"
        )
        self.scale1.configure(tickinterval="1.0", to="10")
        self.scale1.grid(column="0", columnspan="2", row="1")
        self.frame1.configure(height="200", padx="50", pady="50", width="200")
        self.frame1.pack(side="top")
        # Main widget
        self.mainwindow = self.frame1
        self.root = master
        
    def run(self):
        self.mainwindow.mainloop()
        
    def whitesClicked(self):
        global pColor, cLevel
        pColor = PieceColor.WHITE
        cLevel = self.scale1.get()
        self.root.quit()
        self.root.destroy()
    
    def blacksClicked(self):
        global pColor, cLevel
        pColor = PieceColor.BLACK
        cLevel = self.scale1.get()
        self.root.quit()
        self.root.destroy()

# TODO: Shorten this function
def main():
    global pColor, cLevel
    chess = ChessGame(pColor, cLevel)
    pygame.init()
    icon = pygame.image.load("pieces/white/king.png")
    icon = pygame.transform.scale(icon, (64, 64))
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Chess")
    chess.draw(screen)
    pygame.display.flip()
    # chess.board.fromFEN("rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2")
    draging = False
    done = False
    while not done:
        chess.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                p = chess.posToBoard(event.pos)
                draging = True
                chess.select(p)
                if chess.selected is not None:
                    chess.selected.isDraging = True
                print(chess.avaliableMoves())
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                p = chess.posToBoard(event.pos)
                chess.move(p)
                if chess.selected is not None:
                    chess.selected.isDraging = False
                draging = False
                chess.draw(screen)
                if chess.selected is not None and chess.selected.isMoved:
                    chess.selected.drawPrevious(screen)
                pygame.display.flip()
            if event.type == pygame.MOUSEMOTION and draging:
                chess.drag(screen, event.pos)
                pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    print(chess.board)
                if event.key == pygame.K_r:
                    print(repr(chess.board))
                if event.key == pygame.K_m:
                    print(chess.board.moves)
                if event.key == pygame.K_n:
                    print(chess.board.captured)
                if event.key == pygame.K_f:
                    print(chess.board.toFEN())
                if event.key == pygame.K_q:
                    chess.reset()
                    chess.draw(screen)
                    pygame.display.flip()
    
if __name__ == "__main__":
    root = tk.Tk()
    SCREEN_WIDTH = root.winfo_screenwidth()
    SCREE_HEIGHT = root.winfo_screenheight()
    root.geometry(f"+{SCREEN_WIDTH//2 - 200}+{SCREE_HEIGHT//2 - 200}")
    app = LevelSelection(root)
    app.run()
    main()