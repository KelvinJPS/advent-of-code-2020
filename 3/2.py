if __name__ == "__main__":
    trees = []
    map = []
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    # Read the input map
    with open("input") as input:
        for line in input:
            map.append(line.strip())

    row_len = len(map[0])
    for slope in slopes:
        right = slope[0]
        down = slope[1]
        tree_count = 0
        result = 1
        col = 0

        for row_index in range(0, len(map), down):
            row = map[row_index]
            if row[col] == "#":
                tree_count += 1
            col += right
            if col >= row_len:
                col -= row_len

        trees.append(tree_count)
        for tree in trees:
            result *= tree

    print(result)
    print(trees)
