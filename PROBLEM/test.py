"""coke"""
def main():
    """coke"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    caps = 0
    money = 0
    for _ in range (d):
        if 0 < b <= caps:
            money += c
            caps -= b
        else:
            money += a
        caps += 1
    print(money)
main()
