from collections import Counter


def load_data(file):
    data = [line.strip().split() for line in open(file)]
    return data


def solve_one(a, b):
    total = sum([abs(int(a) - int(b)) for a, b in zip(a, b)])
    return total


def solve_two(a, b):
    b_counts = Counter(b)
    total = sum(int(num) * b_counts[num] for num in a if num in b)

    return total


# data = load_data("sample_input.txt")
data = load_data("input_one.txt")
a, b = map(list, zip(*(d for d in data)))

a.sort()
b.sort()
print(solve_one(a, b), solve_two(a, b))

# data = ...
# with open(file) as f:
#     data = f.readlines()

# sum = 0
# for a, b in zip(a, b):
#     sum += abs(int(a) - int(b))
# num_map = {}
# for count, item in enumerate(a):
#     temp_map = {}
#     for j in b:
#         if j > item:
#             break
#         if j == item:
#             if a[count] in temp_map.keys():
#                 temp_map[item] += 1
#             else:
#                 temp_map[item] = 1
#     num_map = {**num_map, **temp_map}
#
# similarity = [
#     int(item) * int(num_map[item]) for item in a if item in num_map.keys()
# ]
# total = sum(similarity)
