from aocd import submit, get_data


def main():
    day = 1
    year = 2025
    data = get_data(day=day, year=year)

    test_data_a = {
        """L68
           L30
           R48
           L5
           R60
           L55
           L1
           L99
           R14
           L82""": 3,
    }
    test_data_b = {
        """L100""": 1,
        """R100""": 1,
        """R50
           L50""": 1,
        """R50
           L100""": 2,
        """R50
           R100""": 2,
        """R50
           R200""": 3,
        """R50
           L200""": 3,
        """R50
           L1""": 1,
        """R50
           R1""": 1,
        """R50
           R101""": 2,
        """R50
           L101""": 2,
        """R50
           L0""": 1,
        """R50
           R0""": 1,
        """R1000""": 10,
        """L1000""": 10,
        """L28
           L622""": 7,

        """L68
           L30
           R48
           L5
           R60
           L55
           L1
           L99
           R14
           L82""": 6,
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


def solve_a(data, start=50, total=100):
    times = 0
    position = start
    steps = [step.strip() for step in data.splitlines()]
    for step in steps:
        direction, length = step[0], int(step[1:])
        if direction == "L":
            position = (position - length) % total
        else:
            position = (position + length) % total
        if position == 0:
            times += 1

    return times


def solve_b(data, start=50, total=100):
    times = 0
    position = start
    steps = [step.strip() for step in data.splitlines()]
    for step in steps:
        direction, length = step[0], int(step[1:])
        if length == 0:
            continue
        if position == 0 and direction == "L":
            correction = -1
        else:
            correction = 0
        if direction == "L":
            position = position - length
            if position == 0:
                times += 1 + correction
            if position < 0:
                times += abs(position // total) + correction
                if position % total == 0:
                    times += 1
        else:
            position = position + length
            if position == total:
                times += 1 + correction
            if position > total:
                times += position // total + correction
        position %= total

    return times


if __name__ == "__main__":
    main()
