"""Difference of two sets."""
def read_set(count):
    """Read `count` integers, one per line, and return them as a set."""
    return {int(input()) for _ in range(count)}


def main():
    """Difference of two sets."""
    n = int(input())
    m = int(input())

    set_a = read_set(n)
    set_b = read_set(m)

    difference = sorted(set_a - set_b)
    print(" ".join(str(number) for number in difference))
main()
