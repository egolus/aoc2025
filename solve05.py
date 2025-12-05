from aocd import submit, get_data


def main():
    day = 5
    year = 2025
    data = get_data(day=day, year=year)

    test_data_a = {
        """3-5
        10-14
        16-20
        12-18

        1
        5
        8
        11
        17
        32""": 3,
    }
    test_data_b = {
        """3-5
        10-14
        12-18
        16-20
        12-18
        12-18

        1
        5
        8
        11
        17
        32""": 14,
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
    ids = set()
    data = data.split("\n\n")
    ranges = data[0]
    targets = data[1]
    for r in (x.strip() for x in ranges.splitlines()):
        r = r.split("-")
        f = int(r[0])
        t = int(r[1])
        ids.add((f, t))
    for t in (x.strip() for x in targets.splitlines()):
        for i in ids:
            if i[0] <= int(t) <= i[1]:
                count += 1
                break
    return count


def solve_b(data):
    ids = list()
    data = data.split("\n\n")
    ranges = data[0]
    for r in (x.strip() for x in ranges.splitlines()):
        r = r.split("-")
        f = int(r[0])
        t = int(r[1])
        ids.append([f, t])
    ids.sort()

    for k in range(len(ids)-1, 0, -1):
        if ids[k] == ids[k-1]:
            ids.pop(k)

    for k in range(2):
        for i in ids:
            for j in ids:
                if i == j:
                    continue
                if j[0] <= i[1] <= j[1]:
                    if j[0] <= i[0] <= j[1]:
                        i[0] = 0
                        i[1] = 0
                    else:
                        i[1] = j[0]-1
    for k in range(len(ids)-1, -1, -1):
        if ids[k][0] == 0 and ids[k][1] == 0:
            ids.pop(k)

    return sum(i[1] - i[0] for i in ids) + len(ids)


if __name__ == "__main__":
    main()
