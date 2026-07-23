def main():
    num = int(input())
    t = num - 1
    m = 1
    while True:
        if m * m >= t:
            print(2 * m - 2)
            return
        if m * (m + 1) >= t:
            print(2 * m - 1)
            return
        m += 1

main()