"""arcade"""
def main():
    """arcade"""
    num, check = map(int, input().split())
    check += 0
    stores = []
    for _ in range(num):
        start, stop = map(int, input().split())
        stores.append((start, stop))
    times = list(map(int, input().split()))
    answers = []
    for time in times:
        count = 0
        for start, stop in stores:
            if start <= time < stop:
                count += 1
        answers.append(count)
    print(*answers)
main()
