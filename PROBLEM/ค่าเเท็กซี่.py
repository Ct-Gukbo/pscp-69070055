"""taxi"""
def main():
    """taxi"""
    kilo = int(input())
    money = 35
    for _ in range(kilo):
        if kilo == 1:
            money += 0
        elif 1 <= kilo <= 10:
            money += 5
        elif kilo > 10:
            money += 8
    print(money)
main()
