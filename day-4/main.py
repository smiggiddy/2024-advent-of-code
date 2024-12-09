def load_data(file):
    return [[*map(lambda x: x, line.strip())] for line in open(file)]


def search_diag(y, x, grid, target):
    count = 0
    max_x = len(grid[0])
    max_y = len(grid)
    direction = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

    def check_bounds(x, y):
        return 0 <= x < max_x and 0 <= y < max_y

    for d in direction:
        word = ""
        for i in range(len(target)):
            ny, nx = d[0] * i + y, d[1] * i + x
            if check_bounds(ny, nx):
                word += grid[ny][nx]

        if word == target:
            count += 1

    return count


def solve_one(grid):
    x_max = len(grid[0])
    y_max = len(grid)

    total = 0
    for y in range(y_max):
        for x in range(x_max):
            total += search_diag(y, x, grid, "XMAS")

            if x + 3 < x_max:
                word_horizontal = (
                    grid[y][x] + grid[y][x + 1] + grid[y][x + 2] + grid[y][x + 3]
                )
                if word_horizontal == "XMAS" or word_horizontal == "SAMX":
                    total += 1

            if y + 3 < y_max:
                word_vertical = (
                    grid[y][x] + grid[y + 1][x] + grid[y + 2][x] + grid[y + 3][x]
                )
                if word_vertical == "XMAS" or word_vertical == "SAMX":
                    total += 1

    print(total)


def solve_two(grid):
    total = 0
    x_max = len(grid[0])
    y_max = len(grid)

    valid_set = {("M", "S"), ("S", "M")}

    for y in range(y_max):
        for x in range(x_max):

            if grid[y][x] == "A" and 0 < x < x_max - 1 and 0 < y < y_max - 1:

                if all(
                    [
                        (grid[y - 1][x - 1], grid[y + 1][x + 1]) in valid_set,
                        (grid[y + 1][x - 1], grid[y - 1][x + 1]) in valid_set,
                    ]
                ):
                    total += 1

    print(total)


def main():
    # data = load_data("./input_test.txt")
    # data = load_data("./input_test2.txt")
    data = load_data("./input.txt")

    solve_one(data)
    solve_two(data)


main()
