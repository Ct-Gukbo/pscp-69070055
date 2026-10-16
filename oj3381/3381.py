"""Point Sorting"""
def read_points(count):
    """Read `count` lines of 'x y' and return a list of (x, y)."""
    points = []
    for _ in range(count):
        x, y = map(int, input().split())
        points.append((x, y))
    return points


def sort_key(point):
    """Sort by x + y ascending, then by y descending."""
    x, y = point
    return (x + y, -y)


def main():
    """Point Sorting"""
    test_cases = int(input())

    for _ in range(test_cases):
        count = int(input())
        points = read_points(count)

        for x, y in sorted(points, key=sort_key):
            print(x, y)


main()
