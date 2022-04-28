import solve
# import window


table = [
        [" ", "0", " ", " ", " ", "1", " ", " ", "4"],
        ["1", " ", " ", " ", "2", " ", " ", "5", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", "5", " ", "0", " ", " ", " ", " "],
        ["9", " ", " ", " ", " ", "8", " ", "3", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", "2", " ", " ", " ", "0", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", "6", " "],
        ["8", " ", " ", " ", "7", " ", " ", " ", " "]
    ];

def draw_table(table):
    for i, row in enumerate(table):
        if i % 3 == 0 and i != 0:
            print("===========❚===========❚===========");
        elif i != 0:
            print("---+---+---❚---+---+---❚---+---+---");
        
        for j, col in enumerate(row):
            if (j + 1) % 3 == 0 and j != 8:
                print(f" {col} ", end="❚");
            elif j == 8:
                print(f" {col} ", end=" ");
            else:
                print(f" {col} ", end="|");
        print();

def main():
    solver = solve(table);
    solver.solve();


if __name__ == "__main__":
    main()