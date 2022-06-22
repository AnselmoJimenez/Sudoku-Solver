import pygame
import sudoku
from constants import WINDOW_WIDTH, WINDOW_HEIGHT
from constants import LIGHTGRAY

class window:
    def __init__(self):
        self.FPS = 60;
        self.WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT));
        pygame.display.set_caption(" Sudoku Solver");

        self.game_loop();

    def game_loop(self):
        game = sudoku.sudoku();

        clock = pygame.time.Clock();
        run = True;
        while run:
            clock.tick(self.FPS);
            for event in pygame.event.get():
                # If exit the window, quit
                if event.type == pygame.QUIT: run = False;
            
            game.draw_board(self.WINDOW);
            pygame.display.update();

        
        pygame.quit();
        return;

    