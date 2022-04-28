import solve
import window


def define_table():
    return [
        [" ", "0", " ", " ", " ", "1", " ", " ", "4"],
        ["1", " ", " ", " ", "2", " ", " ", "5", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", "5", " ", "0", " ", " ", " ", " "],
        ["9", " ", " ", " ", " ", "8", " ", "3", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", "2", " ", " ", " ", "0", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", "6", " "],
        ["8", " ", " ", " ", "7", " ", " ", " ", " "]
    ]

# ❚
def draw_table(table):
    for i, row in enumerate(table):
        if i % 3 == 0 and i != 0:
            print("===========❚===========❚===========");
        elif i != 0:
            print("---+---+---❚---+---+---❚---+---+---");
        
        for j, col in enumerate(row):
            print(f" {col} ", end="❚" if (j + 1) % 3 == 0 and j != 8 else " " if j == 8 else "|");
        print();



def main():
    draw_table(define_table())

if __name__ == "__main__":
    main()