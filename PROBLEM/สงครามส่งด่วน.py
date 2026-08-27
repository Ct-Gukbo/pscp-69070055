"""สงครามส่งด่วน"""
def main():
    """สงครามส่งด่วน"""
    inout = input().split(" ")
    weight = float(input())
    ins = inout[0]
    out = inout[1]
    money = 0
    if ins == "BKK" and out == "CNX":
        money += 10
        money += weight * 30
        print(f"{money:.2f}")
    elif ins == "CNX" and out == "UBP":
        money += 15
        money += weight *40
        print(f"{money:.2f}")
    elif ins == "UBP" and out == "BKK":
        money += 20
        money += weight *40
        print(f"{money:.2f}")
    elif ins == "BKK" and out == "PKT":
        money += 25
        money += weight *50
        print(f"{money:.2f}")
    elif ins == "PKT" and out == "CNX":
        money += 30
        money += weight *60
        print(f"{money:.2f}")
    elif ins == "UBP" and out == "PKT":
        money += 40
        money += weight *70
        print(f"{money:.2f}")
    else:
        print("Error")
main()
