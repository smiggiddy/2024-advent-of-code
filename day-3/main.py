import re


def get_data(path):
    with open(path) as f:
        data = f.readlines()

        return "".join(data)


def solve_one(data):

    pattern = r"mul\(\d+,\d+\)"

    match = re.findall(pattern, data)

    nums = [*map(lambda x: x.strip("mul(").strip(")").split(","), match)]

    sums = sum([int(x) * int(y) for x, y in nums])

    return sums


def solve_two(data):
    parts = re.split(r"(don't\(\)|do\(\))", data)
    process_muls = True
    sums = 0

    for part in parts:
        lower_part = part.lower()

        if lower_part == "don't()":
            process_muls = False
        elif lower_part == "do()":
            process_muls = True
        elif process_muls:
            sums += solve_one(lower_part)

    return sums


def main():
    # data = get_data("./input_test_2.txt")
    data = get_data("input.txt")

    print(solve_one(data))
    print(solve_two(data))


main()
