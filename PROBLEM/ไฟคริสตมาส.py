"""ไฟคริสตมาส"""
def main():
    """ไฟคริสตมาส"""
    start_color, count_str = input().split()
    count = int(count_str)
    colors = ["Red", "Green", "Blue"]
    color_map = {"R": 0, "G": 1, "B": 2}
    start_index = color_map[start_color.upper()]
    result = []
    for i in range(count):
        current_index = (start_index + i) % 3
        result.append(colors[current_index])
    print(" ".join(result))
main()
