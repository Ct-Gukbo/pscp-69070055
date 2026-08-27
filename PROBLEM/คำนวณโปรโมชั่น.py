"""คำนวณราคาสินค้าโปรโมชั่น"""
def main():
    """คำนวณราคาสินค้าโปรโมชั่น"""
    All = input().split(" ")
    a = int(All[0])
    b = int(All[1])
    c = int(All[2])
    money = 0
    if a > 0:
        money += a * 25
    if b > 0:
        money += b * 40
    if c > 0:
        money += c * 55
    if (a + b + c) >= 3:
        print(int(money * 0.90))
    else:
        print(money)
main()
