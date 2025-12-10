from aocd import submit, get_data


def main():
    day = 9
    year = 2025
    data = get_data(day=day, year=year)

    test_data_a = {
        """7,1
        11,1
        11,7
        9,7
        9,5
        2,5
        2,3
        7,3""": 50,
    }
    test_data_b = {
        """7,1
        11,1
        11,7
        9,7
        9,5
        2,5
        2,3
        7,3""": 24,
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
    maxsize = 0
    tiles = []

    maxx, maxy = 0, 0
    for line in data.splitlines():
        x, y = line.strip().split(",")
        x, y = int(x), int(y)
        maxx = max(x, maxx)
        maxy = max(y, maxy)
        tiles.append((x, y))

    for i in range(len(tiles)-1):
        t1 = tiles[i]
        for j in range(i+1, len(tiles)):
            t2 = tiles[j]
            size = (abs(t1[0]-t2[0])+1) * (abs(t1[1]-t2[1])+1)
            maxsize = max(size, maxsize)

    return maxsize


def solve_b(data):
    tiles = []
    sizes = []

    maxx, maxy = 0, 0
    for line in data.splitlines():
        x, y = line.strip().split(",")
        x, y = int(x), int(y)
        maxx = max(x, maxx)
        maxy = max(y, maxy)
        tiles.append((x, y))

    greens = set()
    for i in range(len(tiles)):
        t1 = tiles[i]
        t2 = tiles[(i+1) % len(tiles)]
        if t1[0] == t2[0]:
            l = min(t1[1], t2[1])
            h = max(t1[1], t2[1])
            for k in range(l, h+1):
                greens.add((t1[0], k))
        else:
            l = min(t1[0], t2[0])
            h = max(t1[0], t2[0])
            for k in range(l, h+1):
                greens.add((k, t1[1]))

    for i in range(len(tiles)-1):
        t1 = tiles[i]
        for j in range(i+1, len(tiles)):
            t2 = tiles[j]
            size = (abs(t1[0]-t2[0])+1) * (abs(t1[1]-t2[1])+1)
            sizes.append((size, t1, t2))

    sizes.sort(reverse=True)

    for size, t1, t2 in sizes:
        for t3 in greens:
            if (((t1[0] < t3[0] < t2[0]) or (t2[0] < t3[0] < t1[0]))
                    and
                    ((t1[1] < t3[1] < t2[1]) or (t2[1] < t3[1] < t1[1]))):
                break
        else:
            return size


if __name__ == "__main__":
    main()
