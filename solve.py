class solve:
    def __init__(self, table):
        self.table = table;
        self.row = 0;
        self.col = 0;
        self.solved = False;

    def draw_table(self, table):
        for i, row in enumerate(table):
            if i % 3 == 0 and i != 0:
                print("===========❚===========❚===========");
            elif i != 0:
                print("---+---+---❚---+---+---❚---+---+---");
            
            for j, col in enumerate(row):
                if col == 0: col = " ";
                if (j + 1) % 3 == 0 and j != 8:
                    print(f" {col} ", end="❚");
                elif j == 8:
                    print(f" {col} ", end=" ");
                else:
                    print(f" {col} ", end="|");
            print();
        print();

    def check_validity(self, entry) -> bool:
        if self.check_row(entry) and self.check_col(entry) and self.check_box(entry):
            return True;
        return False;

    def check_row(self, entry) -> bool:
        for element in self.table[self.row]:
            if entry == element:
                return False;
        return True;

    def check_col(self, entry) -> bool:
        for row in self.table:
            if row[self.col] == entry:
                return False;
        return True;

    def check_box(self, entry) -> bool:
        validity = False;
        box_row = self.row - (self.row % 3);
        box_col = self.col - (self.col % 3);
        print(f"Entry: {entry}");
        print(f"Box: {box_row // 3} {box_col // 3}");

        for i in range(3):
            for j in range(3):
                print(f"Checking position: {i + box_row} {j + box_col}");
                if self.table[i + box_row][j + box_col] == entry:
                    validity = False;
                    return validity;
                else:
                    validity = True;
        print();
        return validity;

    def insert_entry(self, entry):
        self.table[self.row][self.col] = entry;

    def update_pos(self):
        self.col += 1;

        if self.col == 9 and self.row == 9:
            self.solved = True;
        elif self.col == 9:
            self.col = 0;
            self.row += 1;
        
        print(f"current position: {self.row} {self.col}");

    def run(self, row, col):
        self.draw_table(self.table);

        if self.table[self.row][self.col] != 0:
            self.update_pos();
            if self.solved != True:
                self.run(self.row, self.col);

        else:
            for i in range(9):
                if self.check_validity(i + 1):
                    self.insert_entry(i + 1);
                    self.update_pos();
                    if self.solved != True:
                        self.run(self.row, self.col);
                    else: 
                        break;
                else:
                    