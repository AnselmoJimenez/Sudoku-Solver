import window


class solve:
    def __init__(self, table):
        self.table = table;

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

    def check_validity(self, entry, row, col) -> bool:
        if self.check_row(entry, row) and self.check_col(entry, col) and self.check_box(entry, row, col):
            return True;
        return False;

    def check_row(self, entry, row) -> bool:
        for element in self.table[row]:
            if entry == element:
                return False;
        return True;

    def check_col(self, entry, col) -> bool:
        for row in self.table:
            if row[col] == entry:
                return False;
        return True;

    def check_box(self, entry, row, col) -> bool:
        box_row = row - (row % 3);
        box_col = col - (col % 3);

        for i in range(3):
            for j in range(3):
                if self.table[i + box_row][j + box_col] == entry:
                    return False;
        return True;

    def insert_entry(self, entry, row, col):
        self.table[row][col] = entry;

    def run(self, row, col):
        self.draw_table(self.table);

        if row == 8 and col == 9:
            return True;

        if col == 9:
            col = 0;
            row += 1;

        print(f"Checking position: {row} {col}");

        if self.table[row][col] != 0:
            if self.run(row, col + 1):
                return True;
        else:
            for i in range(9):
                if self.check_validity(i + 1, row, col):
                    self.insert_entry(i + 1, row, col);
                    if self.run(row, col + 1):
                        return True;
                self.table[row][col] = 0;
        return False;
