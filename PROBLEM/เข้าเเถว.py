"""เข้าเเถว"""
def main():
    """เข้าเเถว"""
    n, _ = map(int, input().split())
    heights = list(map(int, input().split()))
    positions = list(map(int, input().split()))

    prefix_max = [0] * (n + 1)
    for i in range(n):
        prefix_max[i + 1] = max(prefix_max[i], heights[i])

    for position in positions:
        if position == 1:
            print(0)
        else:
            tallest_front = prefix_max[position - 1]
            height = heights[position - 1]
            print(max(0, tallest_front - height + 1))
main()
