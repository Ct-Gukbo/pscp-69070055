"""Array 2D ตรวจสอบ"""
SIZE = 5
def find_odd_index(sums):
    """Return the index of the first odd sum, or -1 if none."""
    for index, total in enumerate(sums):
        if total % 2 == 1:
            return index
    return -1


def main():
    """Array 2D ตรวจสอบ"""
    grid = [list(map(int, input().split())) for _ in range(SIZE)]

    row_sums = [sum(row) for row in grid]
    column_sums = [
        sum(grid[row][column] for row in range(SIZE))
        for column in range(SIZE)
    ]

    odd_row = find_odd_index(row_sums)
    odd_column = find_odd_index(column_sums)

    if odd_row == -1 or odd_column == -1:
        print("-1 -1")
    else:
        print(odd_row, odd_column)


main()
