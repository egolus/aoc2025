from math import sqrt
from aocd import submit, get_data


def main():
    day = 8
    year = 2025
    data = get_data(day=day, year=year)

    test_data_a = {
        ("""162,817,812
        57,618,57
        906,360,560
        592,479,940
        352,342,300
        466,668,158
        542,29,236
        431,825,988
        739,650,466
        52,470,668
        216,146,977
        819,987,18
        117,168,530
        805,96,715
        346,949,466
        970,615,88
        941,993,340
        862,61,35
        984,92,344
        425,690,689""", 10): 40,
    }
    test_data_b = {
        """162,817,812
        57,618,57
        906,360,560
        592,479,940
        352,342,300
        466,668,158
        542,29,236
        431,825,988
        739,650,466
        52,470,668
        216,146,977
        819,987,18
        117,168,530
        805,96,715
        346,949,466
        970,615,88
        941,993,340
        862,61,35
        984,92,344
        425,690,689""": 25272,
    }

    for i, (test, true) in enumerate(test_data_a.items()):
        result = solve_a(*test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_a = solve_a(data, 1000)
    print(f"result a: {result_a}\n")
    submit(result_a, part="a", day=day, year=year)

    for i, (test, true) in enumerate(test_data_b.items()):
        result = solve_b(test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_b = solve_b(data)
    print(f"result b: {result_b}\n")
    submit(result_b, part="b", day=day, year=year)


def dist(a, b):
    return sqrt(
            (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2
        )


def solve_a(data, times):
    boxes = set()
    curcuits = []
    distances = dict()
    for line in data.splitlines():
        x, y, z = line.strip().split(",")
        boxes.add((int(x), int(y), int(z)))
        curcuits.append([(int(x), int(y), int(z))])

    for a in boxes:
        for b in boxes:
            if a == b:
                continue
            if (b, a) in distances:
                continue
            distances[(a, b)] = dist(a, b)

    distances = [k for k, v in sorted(distances.items(), key=lambda x: x[1])]

    t = 0
    while t < times:
        curcuits.sort(key=lambda x: len(x), reverse=True)
        t += 1

        a, b = distances.pop(0)

        found = False
        for c in curcuits:
            if found:
                break
            if a in c:
                if b in c:
                    # t -= 1
                    break
                for c2 in curcuits:
                    if c2 == c:
                        continue
                    if b in c2:
                        c.extend(c2)
                        curcuits.remove(c2)
                        found = True
                        break

    curcuits.sort(key=lambda x: len(x), reverse=True)
    total = 1
    for c in curcuits[:3]:
        total *= len(c)

    return total


def solve_b(data):
    boxes = set()
    curcuits = []
    distances = dict()
    for line in data.splitlines():
        x, y, z = line.strip().split(",")
        boxes.add((int(x), int(y), int(z)))
        curcuits.append([(int(x), int(y), int(z))])

    for a in boxes:
        for b in boxes:
            if a == b:
                continue
            if (b, a) in distances:
                continue
            distances[(a, b)] = dist(a, b)

    distances = [k for k, v in sorted(distances.items(), key=lambda x: x[1])]

    t = 0
    while len(curcuits) > 1:
        curcuits.sort(key=lambda x: len(x), reverse=True)
        t += 1

        a, b = distances.pop(0)

        found = False
        for c in curcuits:
            if found:
                break
            if a in c:
                if b in c:
                    # t -= 1
                    break
                for c2 in curcuits:
                    if c2 == c:
                        continue
                    if b in c2:
                        c.extend(c2)
                        curcuits.remove(c2)
                        found = True
                        break

    return a[0] * b[0]


if __name__ == "__main__":
    main()
