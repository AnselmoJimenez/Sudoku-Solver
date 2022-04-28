class solve:
    def __init__(self, table):
        self.table = table;
        self.row = 0;
        self.col = 0;
        self.pos = self.table[self.row][self.col];

    def check_validity(self, entry) -> bool:
        pass

    def check_row(self, pos) -> bool:
        pass

    def check_col(self, pos) -> bool:
        pass

    def check_box(self, pos) -> bool:
        pass

    def insert_entry(self, entry):
        self.table[self.row][self.col] = entry;

    def update_pos(self, row, column):
        # if at last row, only update column
        if self.row == 8:
            self.col += 1;

        # if at end of the column, update row and column
        elif self.col == 8:
            self.row += 1;
            self.col = 0;

        # If at the end of the table
        elif self.col == 8 and self.row == 8: # end of table
            pass

    
    def solve(self, position, row, col):
        if self.pos != " ": 
            self.update_pos(self.row, self.column); 
            self.solve(self.pos, self.row, self.col);

        for i in range(9):
            self.insert_entry(i);
            # Validate entry