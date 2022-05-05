import solve
# import window

TABLE = [
        [0, 3, 0, 0, 0, 1, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 2, 0, 0, 5, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 8, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 7, 0, 0, 0, 0]
    ];



def main():
    solver = solve.solve(TABLE);
    solver.run(0, 0);


if __name__ == "__main__":
    main()