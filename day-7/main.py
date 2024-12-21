# I was stuck so I reviewed solutions
# https://dev.to/grantdotdev/aoc-24-day7-bridge-repair-n7n
def load_data(file):
    return [line.strip().split(": ") for line in open(file)]


def equals_target(mark: int, numbers: list):
    def calibration(index, current):
        if index == len(numbers):
            return current == mark

        if calibration(index + 1, current + numbers[index]):
            return True

        if calibration(index + 1, current * numbers[index]):
            return True

        # part 2

        concat_value = int(str(current) + str(numbers[index]))
        if calibration(index + 1, concat_value):
            return True

        return False

    return calibration(1, numbers[0])


def solve_one(data):
    total = 0
    for k, v in data:
        total += k if equals_target(k, v) else 0

    print(total)


def main():
    data = load_data("./input.txt")
    # data = load_data("./test_input.txt")
    val = [(int(item[0]), [*map(int, item[1].split(" "))]) for item in data]
    # val = [(item[0], item[1].split(" ")) for item in data]

    solve_one(val)


if __name__ == "__main__":
    main()

# def expressions(values):
#     expr = set()
#
#     for val in permutations(values, len(values)):
#         for op_combo in combinations_with_replacement(operators, len(values) - 1):
#             for op in permutations(op_combo, len(values) - 1):
#                 formula = "".join(o + str(v) for o, v in zip([""] + list(op), values))
#                 expr.add(formula)
#
#     return expr
# total = 0
# for _, p in enumerate(data):
#     a = p[0]
#
#     # get the simple ones out the way
#     if sum(p[1]) == a or prod(p[1]) == a:
#         total += a
#         continue
#
#     for expr in expressions(p[1]):
#         val = result(expr)
#         if val == p[0]:
#             total += val
#             print(f"adding total {val} {expr}")
#             break
#
#
#
#
# def result(expr):
#     e = re.split(r"(\+|\*)", expr)
#     total = 0
#
#     op = ""
#     for i in e:
#         if i == "*" or i == "+" and i != 0:
#             op = i
#             continue
#
#             total += int(i)
#
#     print(total)
#
#     return total
