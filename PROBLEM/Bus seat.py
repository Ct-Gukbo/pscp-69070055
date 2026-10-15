"""Bus seat"""
def seat_label(number, target):
    """Return 'XX' for the target seat, else a 2-digit number."""
    if number == target:
        return "XX"
    return f"{number:02d}"

def main():
    """Bus seat"""
    seats_per_row = int(input())
    row_count = int(input())
    target = int(input())

    for position in range(seats_per_row - 1, -1, -1):
        labels = []
        for row in range(row_count):
            number = row * seats_per_row + position + 1
            labels.append(seat_label(number, target))
        print(" ".join(labels))

        if not position % 2 and position > 0:
            print()

main()
