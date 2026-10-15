"""Array ฮาเฮ"""
ARRAY_SIZE = 50
INPUT_COUNT = 3
def join_numbers(numbers):
    """Return numbers as a space-separated string."""
    return " ".join(str(number) for number in numbers)


def main():
    """Array ฮาเฮ"""
    storage = [0] * ARRAY_SIZE

    for index in range(INPUT_COUNT):
        storage[index] = int(input())
        print(f"Input number {index + 1} stored.")

    data = storage[:INPUT_COUNT]

    while True:
        choice = int(input())

        if not choice:
            break
        if choice == 1:
            print("Original order:", join_numbers(data))
        elif choice == 2:
            print("Descending order:",
                  join_numbers(sorted(data, reverse=True)))
        elif choice == 3:
            print("Ascending order:", join_numbers(sorted(data)))


main()
