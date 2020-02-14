postion = []


def read_input_into_map():
    map = []
    f = open("map.txt", "r")
    lines = f.readlines()
    for line in lines:
        tmp = []
        for c in line:
            if c is not "\n":
                tmp.append(c)
        map.append(tmp)
    return map


def find_char(map, char):
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] is char:
                return row, col  # arrays start at 0...


def move():
    pass


def check_direction(map, directions, position):
    pass


def try_direction(map, dir, position):
    if dir is "S":
        if map[position[0] + 1][position[1]] is not "#":
            print("S", end="")
            return position[0] + 1, position[1]
        else:
            return None
    if dir is "N":
        if map[position[0] - 1][position[1]] is not "#":
            print("N", end="")
            return position[0] - 1, position[1]
        else:
            return None
    if dir is "E":
        if map[position[0]][position[1] + 1] is not "#":
            print("E", end="")
            return position[0], position[1] + 1
        else:
            return None
    if dir is "W":
        if map[position[0]][position[1] - 1] is not "#":
            print("W", end="")
            return position[0], position[1] - 1
        else:
            return None


def reverse_direction(direction_order):
    if (direction_order[0] is "S"):
        direction_order = ['W', 'N', 'E', 'S']
    else:
        direction_order = ["S", "E", "N", "W"]
    return direction_order


def main():
    map = read_input_into_map()
    data_const = "@"
    exit_const = "$"
    position = find_char(map, data_const)
    exit = find_char(map, exit_const)
    direction_order = ["S", "E", "N", "W"]
    cur_char = " "
    direction = "S"
    while position is not exit:
        if cur_char is "I":
            direction_order = reverse_direction(direction_order)

        if position is (2,3):
            print("")
        if try_direction(map, direction, position) is None or map[try_direction(map, direction, position)[0]][try_direction(map, direction, position)[1]] in ["S", "E", "N", "W"]:
            if cur_char in ["S", "E", "N", "W"]:
                position = try_direction(map, cur_char, position)
            else:
                state = None
                i = 0
                while state is None:
                    state = try_direction(map, direction_order[i], position)
                    i = i + 1
                position = state
                direction = direction_order[i]
        else:
            position = try_direction(map, direction, position)

        if position is (2,3):
            print("")
        cur_char = map[position[0]][position[1]]
        print(position)
    print(position)


main()
