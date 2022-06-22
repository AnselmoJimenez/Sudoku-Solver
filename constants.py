# Window Constants
WINDOW_WIDTH = 700;
WINDOW_HEIGHT = 500;

# Board Constants
BOARD_WIDTH = 400;
BOARD_HEIGHT = 400;
ROWS = 9;
COLUMNS = 9;
SQUARE_SIZE = BOARD_WIDTH // COLUMNS;
LINE_SIZE = SQUARE_SIZE * COLUMNS;
OFFSET = 50;

# RGB Colors
LIGHTGRAY = (211, 211, 211);
BLACK = (0, 0, 0);
WHITE = (255, 255, 255);

def calculate_square(row=0, column=0):
    x_coord = column * SQUARE_SIZE + OFFSET;
    y_coord = row * SQUARE_SIZE + OFFSET;
    return (x_coord, y_coord, SQUARE_SIZE, SQUARE_SIZE);
