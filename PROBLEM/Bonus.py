"""Bonus"""
def main():
    """Bonus"""
    Full = input().split(" ")
    Class = str(Full[0])
    Exp = int(Full[1])
    Income = int(Full[2])
    money = 0
    if Class == "M":
        money += 1500
        if Exp <= 5:
            money += (Income * 0.06)
        elif 5 < Exp <= 10:
            money += (Income * 0.08)
        else:
            money += (Income * 0.10)
    elif Class == "B":
        money += 1000
        if Exp <= 5:
            money += (Income * 0.05)
        elif 5 < Exp <= 10:
            money += (Income * 0.06)
        else:
            money += (Income * 0.07)
    elif Class == "G":
        money += 500
        if Exp <= 5:
            money += (Income * 0.04)
        elif 5 < Exp <= 10:
            money += (Income * 0.05)
        else:
            money += (Income * 0.06)
    print(int(money))
main()
