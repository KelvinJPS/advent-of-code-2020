if __name__ == "__main__":
    trees = 0
    map = []
    right = 3
    down = 1
    col = 0

    # Read the input map
    with open("input") as input:
        for line in input:
            map.append(line.strip())

    row_len = len(map[0])

    for row_index in range(0, len(map), down):
        row = map[row_index]
        if row[col] == "#":
            trees += 1
        col += right
        if col >= row_len:
            col -= row_len

    print(trees)
