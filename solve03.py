from aocd import submit, get_data


def main():
    day = 3
    year = 2025
    data = get_data(day=day, year=year)

    test_data_a = {
        """987654321111111
        811111111111119
        234234234234278
        818181911112111""": 357,
    }
    test_data_b = {
        """987654321111111
        811111111111119
        234234234234278
        818181911112111""": 3121910778619,
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
    result = 0
    lines = data.splitlines()
    for line in lines:
        pos0 = 0
        out = ""
        line = line.strip()
        for i in range(9, 0, -1):
            si = str(i)
            if len(out) == 2:
                break
            if si in line:
                try:
                    pos = line.index(si)
                    if out:
                        if pos < pos0:
                            out = si + out
                        else:
                            out += si
                    else:
                        out = si
                        pos0 = pos
                        for j in range(i, 0, -1):
                            if len(out) == 2:
                                break
                            sj = str(j)
                            try:
                                pos = line.index(sj, pos+1)
                                if pos < pos0:
                                    out = sj + out
                                else:
                                    out += sj
                            except ValueError:
                                continue
                except ValueError:
                    continue
        result += int(out)
    return result


def solve_b(data):
    result = 0
    lines = data.splitlines()
    for line in lines:
        line = line.strip()
        tmp = line
        while len(tmp) > 12:
            for pos in range(len(tmp)-1):
                if tmp[pos] < tmp[pos+1]:
                    tmp = tmp[:pos] + tmp[pos+1:]
                    break
            else:
                tmp = tmp[:-1]
        result += int(tmp)
    return result


if __name__ == "__main__":
    main()
