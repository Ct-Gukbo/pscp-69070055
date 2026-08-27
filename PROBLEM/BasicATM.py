"""ATM"""
def main():
    """ATM"""
    money = int(input())
    if money < 100 or money > 20000 or money % 100:
        print("ERROR")
    else:
        bank1000 = money // 1000
        money %= 1000
        bank500 = money // 500
        money %= 500
        bank100 = money // 100
        if bank1000 > 0:
            print("1000 =", bank1000)
        if bank500 > 0:
            print("500 =", bank500)
        if bank100 > 0:
            print("100 =", bank100)
main()
