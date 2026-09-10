"""ระบบคิดคะแนนเกมออนไลน์"""
def main():
    """ระบบคิดคะแนนเกมออนไลน์"""
    base = int(input())
    bonus = int(input())
    days = int(input())
    total = base + bonus
    if days > 3:
        suma = int(total * 1.5)
    else:
        suma = total
    if suma >= 1500:
        pas = 5
    elif suma >= 1000:
        pas = 4
    elif suma >= 500:
        pas = 3
    elif suma >= 200:
        pas = 2
    else:
        pas = 1
    print(suma)
    print(pas)
    if pas == 5 and days >= 7:
        print("99")
    elif pas == 4 and bonus > 300:
        print("88")
    else:
        print("0")
main()
