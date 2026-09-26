"""สมดุลย์ชีวิต"""
def main():
    """สมดุลย์ชีวิต"""
    n = int(input())

    long_count = 0
    short_count = 0

    for _ in range(n):
        h = int(input())
        if h > 18:
            long_count = long_count + 1
        else:
            short_count = short_count + 1

    if long_count > short_count + 1:
        rest_days = long_count - short_count - 1
        days = n + rest_days
    else:
        days = n

    print(days)
main()
