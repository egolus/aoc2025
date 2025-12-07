from aocd import submit, get_data


def main():
    day = 7
    year = 2025
    data = get_data(day=day, year=year)

    test_data_a = {
        """.......S.......
        ...............
        .......^.......
        ...............
        ......^.^......
        ...............
        .....^.^.^.....
        ...............
        ....^.^...^....
        ...............
        ...^.^...^.^...
        ...............
        ..^...^.....^..
        ...............
        .^.^.^.^.^...^.
        ...............""": 21,
    }
    test_data_b = {
        """.......S.......
        ...............
        .......^.......
        ...............
        ......^.^......
        ...............
        .....^.^.^.....
        ...............
        ....^.^...^....
        ...............
        ...^.^...^.^...
        ...............
        ..^...^.....^..
        ...............
        .^.^.^.^.^...^.
        ...............""": 40,
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
    grid = {}
    maxx, maxy = 0, 0

    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line.strip()):
            grid[(y, x)] = c
            maxx = x
        maxy = y

    for y in range(maxy):
        for x in range(maxx):
            if grid[(y, x)] in ("S", "|"):
                if grid[(y+1, x)] == "^":
                    grid[(y+1, x)] = "v"
                else:
                    grid[(y+1, x)] = "|"
            elif grid[(y, x)] == "v":
                # left
                if grid[(y+1, x-1)] == "^":
                    grid[(y+1, x-1)] = "v"
                else:
                    grid[(y+1, x-1)] = "|"
                # right
                if grid[(y+1, x+1)] == "^":
                    grid[(y+1, x+1)] = "v"
                else:
                    grid[(y+1, x+1)] = "|"

    return sum(1 for v in grid.values() if v == "v")


def solve_b(data):
    grid = {}
    maxx, maxy = 0, 0

    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line.strip()):
            grid[(y, x)] = c
            maxx = x
        maxy = y

    for y in range(maxy):
        for x in range(maxx):
            if isinstance(grid[(y, x)], list):
                t, v = grid[(y, x)]
            else:
                t = grid[(y, x)]
                v = 0
            if t == "S":
                grid[(y+1, x)] = ["|", 1]
            if t in ("|",):
                if grid[(y+1, x)] == "^":
                    grid[(y+1, x)] = [grid[(y+1, x)], v]
                elif isinstance(grid[(y+1, x)], list):
                    grid[(y+1, x)][1] += v
                else:
                    grid[(y+1, x)] = ["|", v]
            if t == "^":
                # left
                if grid[(y+1, x-1)] == "^":
                    grid[(y+1, x-1)] = ["^", v]
                elif isinstance(grid[(y+1, x-1)], list):
                    grid[(y+1, x-1)][1] += v
                else:
                    grid[(y+1, x-1)] = ["|", v]
                # right
                if grid[(y+1, x+1)] == "^":
                    grid[(y+1, x+1)] = ["^", v]
                elif isinstance(grid[(y+1, x+1)], list):
                    grid[(y+1, x+1)][1] += v
                else:
                    grid[(y+1, x+1)] = ["|", v]

    return sum(grid[(maxy, x)][1] for x in range(maxx+1)
               if isinstance(grid[(maxy, x)], list))


if __name__ == "__main__":
    main()
