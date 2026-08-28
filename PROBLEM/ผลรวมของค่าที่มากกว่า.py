"""ผลรวมของค่าที่มากกว่า"""
def main():
    """ผลรวมของค่าที่มากกว่า"""
    n = int(input())
    Greater = []
    for i in range (n):
        Num1 = int(input())
        Num2 = int(input())
        if Num1 == Num2:
           Greater.append(Num1)
        elif Num1 > Num2:
            Greater.append(Num1)
        else:
            Greater.append(Num2)
main()