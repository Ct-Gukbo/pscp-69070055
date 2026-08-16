"""inflation"""
def main():
    """inflation"""
    price = float(input())
    year = int(input())
    money = int(price*100)
    for _ in range (year):
        money += (money*381)//10000
    print(f"{money//100}.{money%100:02}")
main()
