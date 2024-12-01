def load_data(file):
    data = ...
    with open(file) as f:
        data = f.readlines()

    data = [line.strip().split() for line in data]
    return data


def clean_data(data):
    list_one = []
    list_two = []

    for _, a in enumerate(data):
        list_one.append(a[0])
        list_two.append(a[1])

    return list_one, list_two


def compare(a, b):
    return abs(int(a) - int(b))


def solve_one(a, b):
    sum = 0
    for a, b in zip(a, b):
        sum += compare(a, b)

    print(sum)
    return sum


def solve_two(a, b):

    num_map = {}
    for count, item in enumerate(a):
        temp_map = {}
        for j in b:
            if j > item:
                break
            if j == item:
                if a[count] in temp_map.keys():
                    temp_map[item] += 1
                else:
                    temp_map[item] = 1
        num_map = {**num_map, **temp_map}

    similarity = [
        int(item) * int(num_map[item]) for item in a if item in num_map.keys()
    ]
    print(similarity)
    return sum(similarity)


# data = load_data("sample_input.txt")
data = load_data("input_one.txt")
a, b = clean_data(data)

a.sort()
b.sort()
solve_one(a, b)
solve_two(a, b)
