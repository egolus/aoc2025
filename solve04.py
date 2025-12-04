from aocd import submit, get_data

from pprint import pprint


def main():
    day = 4
    year = 2025
    data = get_data(day=day, year=year)

    test_data_a = {
        """..@@.@@@@.
           @@@.@.@.@@
           @@@@@.@.@@
           @.@@@@..@.
           @@.@@@@.@@
           .@@@@@@@.@
           .@.@.@.@@@
           @.@@@.@@@@
           .@@@@@@@@.
           @.@.@@@.@.""": 13,
    }
    test_data_b = {
        """..@@.@@@@.
           @@@.@.@.@@
           @@@@@.@.@@
           @.@@@@..@.
           @@.@@@@.@@
           .@@@@@@@.@
           .@.@.@.@@@
           @.@@@.@@@@
           .@@@@@@@@.
           @.@.@@@.@.""": 43,
    }

    for i, (test, true) in enumerate(test_data_a.items()):
        result = solve_a(test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_a = solve_a(data)
    print(f"result a: {result_a}\n")
    submit(result_a, part="a", day=day, year=year)

    for i, (test, true) in enumerate(test_data_b.items()):
        result = solve_b(test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_b = solve_b(data)
    print(f"result b: {result_b}\n")
    submit(result_b, part="b", day=day, year=year)


def solve_a(data):
    count = 0
    maxx, maxy = 0, 0
    grid = {}
    for y, line in enumerate(x.strip() for x in data.splitlines()):
        maxy = y+1
        for x, c in enumerate(line):
            maxx = x+1
            grid[(y, x)] = c

    for y in range(maxy):
        for x in range(maxx):
            rcount = 0
            if grid[(y, x)] == "@":
                for yy in [-1, 0, 1]:
                    for xx in [-1, 0, 1]:
                        if (y+yy, x+xx) in grid:
                            if grid[(y+yy, x+xx)] == "@":
                                rcount += 1
                if rcount < 5:
                    count += 1
    return count


def printgrid(grid, maxy, maxx):
    for y in range(maxy):
        for x in range(maxx):
            print(grid[(y, x)], end="")
        print()


def solve_b(data):
    count = 0
    maxx, maxy = 0, 0
    grid = {}
    for y, line in enumerate(x.strip() for x in data.splitlines()):
        maxy = y+1
        for x, c in enumerate(line):
            maxx = x+1
            grid[(y, x)] = c

    while True:
        # printgrid(grid, maxy, maxx)

        changed = False
        for y in range(maxy):
            for x in range(maxx):
                rcount = 0
                if grid[(y, x)] == "@":
                    for yy in [-1, 0, 1]:
                        for xx in [-1, 0, 1]:
                            if (y+yy, x+xx) in grid:
                                if grid[(y+yy, x+xx)] == "@":
                                    rcount += 1
                    if rcount < 5:
                        changed = True
                        grid[(y, x)] = "x"
        if not changed:
            break
    for y in range(maxy):
        for x in range(maxx):
            if grid[(y, x)] == "x":
                count += 1

    return count


if __name__ == "__main__":
    main()
