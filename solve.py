class solve:
    def __init__(self, table):
        self.table = table;
        self.row = 0;
        self.col = 0;

    def check_validity(self, entry) -> bool:
        pass

    def check_row(self, entry) -> bool:
        for element in self.table[self.row]:
            if entry == element:
                return False;
        return True;

    def check_col(self, entry) -> bool:
        for row in self.table:
            if row[0] == entry:
                return False;
        return True;

    def check_box(self, entry) -> bool:
        box_row = self.row - (self.row % 3);
        box_col = self.col - (self.col % 3);

        for i in range(9):
            for j in range(9):
                if self.table[i + box_row][j + box_col] == entry:
                    return False;
        return True;

    def insert_entry(self, entry):
        self.table[self.row][self.col] = entry;

    def update_pos(self, row, column):
        # If at the end of the table
        if self.col == 8 and self.row == 8:
            self.col += 1;

        # if at end of the column, update row and column
        elif self.col == 8:
            self.row += 1;
            self.col = 0;

        # if at last row, only update column
        elif self.row == 8: # end of table
            pass
    
    def solve(self, position, row, col):
        if self.pos != " ": 
            self.update_pos(self.row, self.column); 
            self.solve(self.pos, self.row, self.col);

        for i in range(9):
            pass
            # Validate entry