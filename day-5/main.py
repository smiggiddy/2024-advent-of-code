def read_input(file):
    with open(file) as f:
        data = f.readlines()

        rules = []
        update = []

        for l in data:
            if "|" in l:
                rules.append(l.strip())
            else:
                if l.strip() == "":
                    continue
                update.append([*map(int, (l.strip().split(",")))])

        return rules, update


def solve_one(r: dict, u: list):

    in_order = True
    sorted = []
    not_sorted = []
    right_pages = []

    for update in u:
        sorted = []
        in_order = True
        while len(sorted) < len(update) and in_order:
            for i, item in enumerate(update):
                if len(sorted) == 0:
                    sorted.append(item)
                    continue
                    # try:
                if item in r[str(sorted[(i - 1)])]:
                    sorted.append(item)
                    continue

                else:
                    current_item_rules = r.get(str(item))
                    if current_item_rules:
                        stop_loop = False
                        for visited in sorted:
                            if visited in current_item_rules:
                                stop_loop = True
                                break
                        if stop_loop:
                            in_order = False
                            break
                        sorted.append(item)
                    else:
                        sorted.append(item)

        if sorted == update:
            middle_index = int(len(sorted) / 2)
            right_pages.append(update[middle_index])
        else:
            not_sorted.append(update)

    solve_sum = sum([*map(int, right_pages)])
    return solve_sum, not_sorted


def custom_sort_manual(update: list, rules: dict):

    finished_sorting = False

    while not finished_sorting:
        visisted = []
        for i in range(len(update) - 1):

            right = rules.get(str(update[i + 1]), "")

            if right:
                if update[i] in right:
                    temp = update[i]
                    update[i] = update[i + 1]
                    update[i + 1] = temp
                else:
                    visisted.append(update[i])
            else:
                visisted.append(update[i])
        if len(visisted) == len(update) - 1:
            finished_sorting = True

    return update


def solve_two(update, rules):
    score = []

    for un in update:
        temp = custom_sort_manual(un, rules)
        middle_index = int(len(temp) / 2)
        score.append(temp[middle_index])

    solve_sum = sum([*map(int, score)])

    return solve_sum


def main():
    # r, u = read_input("./test_input.txt")
    r, u = read_input("./input.txt")
    r.sort()
    r = [i.split("|") for i in r]

    rules = {}

    # use a map for the rules
    for k, v in r:
        if not rules.get(k):
            rules[k] = [int(v)]
        else:
            # rules[k].append(v)
            rules[k].append(int(v))

    right_pages, not_sorted = solve_one(rules, u)
    print(right_pages)
    result = solve_two(not_sorted, rules)
    print(result)

    from functools import cmp_to_key

    rules, pages = open("input.txt").read().split("\n\n")
    cmp = cmp_to_key(lambda x, y: -(x + "|" + y in rules))

    a = [0, 0]
    for p in pages.split():
        p = p.split(",")
        s = sorted(p, key=cmp)
        print(p, s, " p,s")
        a[p != s] += int(s[len(s) // 2])

    print(a)
    print(*a)


main()
