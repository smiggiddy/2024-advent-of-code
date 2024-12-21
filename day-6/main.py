from collections import deque


def load_data(file):
    return [list(line.strip()) for line in open(file)]


def check_exit(pos, max):
    return pos[0] in (0, max[0]) or pos[1] in (0, max[1])


def visited_count(v, cord):
    if cord in v:
        v[cord] += 1
    else:
        v[cord] = 1
    return v


def check_if_loop(v: dict):
    return sum(1 for v in v.values() if v >= 4) >= 2


def bfs(maze: list, pos: tuple, ending: list):
    queue = deque([pos])
    direction = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    ]
    cords = []
    turn_tracking = {}
    good_loop = False

    moves = 0
    direction_index = 0

    while queue:
        current = queue.popleft()

        if check_exit(current, ending):
            maze[current[0]][current[1]] = "X"
            cords.append(current)
            moves += 1
            break

        next_cell = (
            current[0] + direction[direction_index][0],
            current[1] + direction[direction_index][1],
        )

        if 0 <= next_cell[0] < len(maze) and 0 <= next_cell[1] < len(maze[0]):

            if maze[next_cell[0]][next_cell[1]] == "#":
                if direction_index == 3:
                    direction_index = 0
                else:
                    direction_index += 1

                queue.append(current)

                if current in turn_tracking:
                    turn_tracking[current] += 1
                else:
                    turn_tracking[current] = 1

                if check_if_loop(turn_tracking):
                    good_loop = True
                    break

            else:
                queue.append(next_cell)

                if maze[current[0]][current[1]] != "X":
                    maze[current[0]][current[1]] = "X"
                    cords.append(current)

                    moves += 1

    return moves, cords, good_loop


def solve_one(map, start):
    max_x = len(map[0]) - 1
    max_y = len(map) - 1

    ending = [max_y, max_x]

    moves, cords, _ = bfs(map, start, ending)
    print(moves)

    return cords


def solve_two(map: list, start: tuple, cords: list):

    map[start[0]][start[1]] = "^"
    totals = 0

    for _, c in enumerate(list(reversed(cords))):
        test_graph = [row[:] for row in map]

        if c != start and c != (start[0] - 1, start[1]):
            test_graph[c[0]][c[1]] = "#"

        _, _, good_loop = bfs(test_graph, start, [len(map) - 1, len(map[0]) - 1])

        if good_loop:
            totals += 1

    return totals


def main():
    # data = load_data("./test_input.txt")
    data = load_data("./input.txt")

    data_copy = [row[:] for row in data]

    x_len = len(data_copy[0])
    y_len = len(data_copy)

    start = ()
    for i in range(y_len - 1):
        for j in range(x_len - 1):
            if data[i][j] == "^":
                start = (i, j)

    cords = solve_one(data, start)
    total = solve_two(data_copy, start, cords)
    print(total)


if __name__ == "__main__":
    main()
