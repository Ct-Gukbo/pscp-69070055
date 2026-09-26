"""Electric_Using"""
def main():
    """Electric_Using"""
    units = int(input())
    base_cost = 0
    if units <= 10:
        base_cost = units * 5
    elif units <= 50:
        base_cost = 50 + (units - 10) * 7
    elif units <= 100:
        base_cost = 330 + (units - 50) * 10
    elif units <= 200:
        base_cost = 830 + (units - 100) * 12
    else:
        base_cost = 2030 + (units - 200) * 15
    paid = (base_cost*1.07) + units*0.5
    print(f"{paid:.1f}")
main()
