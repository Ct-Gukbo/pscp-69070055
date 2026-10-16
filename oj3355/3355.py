"""Shorten"""
def format_range(start, end):
    """Return a single number"""
    if start == end:
        return str(start)
    return f"{start}-{end}"


def compress(numbers):
    """Return the compressed text for an ascending list of numbers."""
    if not numbers:
        return ""

    parts = []
    start = numbers[0]
    end = numbers[0]

    for number in numbers[1:]:
        if number == end + 1:
            end = number
        else:
            parts.append(format_range(start, end))
            start = number
            end = number

    parts.append(format_range(start, end))
    return ", ".join(parts)


def main():
    """Shorten a list of numbers"""
    numbers = []
    while True:
        number = int(input())
        if number == -1:
            break
        numbers.append(number)
    print(compress(numbers))


main()
