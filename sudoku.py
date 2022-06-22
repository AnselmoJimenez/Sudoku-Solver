import pygame
from constants import LIGHTGRAY, WHITE, BLACK
from constants import BOARD_WIDTH, BOARD_HEIGHT, ROWS, COLUMNS
from constants import SQUARE_SIZE, LINE_SIZE, OFFSET
from constants import calculate_square


class sudoku:
    def __init__(self):
        self.board = [];
        self.selected_box = None;

    # Draw empty board on the surface (window)
    def draw_board(self, window):
        window.fill(LIGHTGRAY);

        # Draw squares
        for row in range(ROWS):
            for column in range(COLUMNS):
                pygame.draw.rect(window, WHITE, calculate_square(row, column), border_radius=10);
        
        # Drawing Lines
        for i in range(1, 3):
            # Drawing Horizontal Lines
            start_coord = (OFFSET, (i * 3) * SQUARE_SIZE + OFFSET);
            end_coord = (OFFSET * LINE_SIZE, (i * 3) * SQUARE_SIZE + OFFSET);
            pygame.draw.line(window, LIGHTGRAY, start_coord, end_coord, width=3);
            # Drawing Vertical Lines
            start_coord = ((i * 3) * SQUARE_SIZE + OFFSET, OFFSET);
            end_coord = ((i * 3) * SQUARE_SIZE + OFFSET, OFFSET * LINE_SIZE);
            pygame.draw.line(window, LIGHTGRAY, start_coord, end_coord, width=3);
