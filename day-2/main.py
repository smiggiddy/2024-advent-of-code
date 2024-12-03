def load_data(file):
    data = [[*map(int, line.strip().split())] for line in open(file)]

    return data


def level_safe(level: list):

    new_list = level.copy()
    current_level = new_list.pop(0)

    if current_level < new_list[0]:
        increasing = True
    else:
        increasing = False

    while len(new_list) != 0:

        difference = 0
        if increasing:
            if current_level > new_list[0]:
                return False
            difference = new_list[0] - current_level
        else:
            if current_level < new_list[0]:
                return False
            difference = current_level - new_list[0]

        if abs(difference) == 0 or abs(difference) > 3:
            return False

        current_level = new_list.pop(0)

    return True


def main():
    # data = load_data("input_test.txt")
    data = load_data("input.txt")
    safe_levels = 0

    for l in data:

        if level_safe(l):
            safe_levels += 1
        # for part two
        # else:
        #     for i in range(len(l)):
        #         temp = l.copy()
        #         temp.pop(i)
        #         if level_safe(temp):
        #             safe_levels += 1
        #             break
    print(safe_levels)


main()
