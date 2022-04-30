import pygame
from game import ChessGame


def main():
    chess = ChessGame()
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
    main()