from aocd import submit, get_data
import functools


def main():
    day = 6
    year = 2025
    data = get_data(day=day, year=year)

    test_data_a = {
        """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """: 4277556,
    }
    test_data_b = {
        """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """: 3263827,
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
    total = 0
    maxx, maxy = 0, 0
    grid = {}
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line.strip().split()):
            grid[(y, x)] = c
            maxx = x + 1
        maxy = y + 1

    for x in range(maxx):
        numbers = [int(grid[(y, x)]) for y in range(maxy-1)]
        if grid[(maxy-1, x)] == "*":
            # multiply
            total += functools.reduce(lambda a, b: a*b, numbers)
        else:
            # add
            total += sum(numbers)

    return total


def solve_b(data):
    total = 0
    maxx, maxy = 0, 0
    grid = {}
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            grid[(y, x)] = c
            maxx = x + 1
        maxy = y + 1

    cols = []
    func = None
    for x in range(maxx):
        col = [grid[(y, x)] for y in range(maxy)]
        if col[-1] != " ":
            func = col[-1]
        if all(c == " " for c in col):
            numbers = [int(''.join(co)) for co in cols]
            if func == "*":
                # multiply
                total += functools.reduce(lambda a, b: a*b, numbers)
            else:
                # add
                total += sum(numbers)
            cols.clear()
        else:
            cols.append(col[:-1])
    numbers = [int(''.join(co)) for co in cols]
    if func == "*":
        # multiply
        total += functools.reduce(lambda a, b: a*b, numbers)
    else:
        # add
        total += sum(numbers)

    return total


if __name__ == "__main__":
    main()
