from aocd import submit, get_data


def main():
    day = 2
    year = 2025
    data = get_data(day=day, year=year)

    test_data_a = {
        """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124""": 1227775554,
    }
    test_data_b = {
        """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124""": 4174379265,
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
    invalid = 0
    data = data.split(",")
    for d in data:
        low, high = d.split("-")
        low, high = int(low), int(high)
        for i in range(low, high+1):
            si = str(i)
            li = len(si)
            if si[:li//2] == si[li//2:]:
                invalid += i
    return invalid


def solve_b(data):
    invalid = 0
    data = data.split(",")
    for d in data:
        low, high = d.split("-")
        low, high = int(low), int(high)
        for i in range(low, high+1):
            si = str(i)
            li = len(si)
            for j in range(1, li//2+1):
                if si == si[:j]*(li//j):
                    invalid += i
                    break
    return invalid


if __name__ == "__main__":
    main()
