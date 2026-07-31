"""วันเกิด"""
from datetime import date
def main():
    """วันเกิด"""
    y1 = int(input())
    m1 = int(input())
    d1 = int(input())

    y2 = int(input())
    m2 = int(input())
    d2 = int(input())

    person1 = date(y1, m1, d1)
    person2 = date(y2, m2, d2)

    diff = abs((person1 - person2).days)

    if diff <= 7:
        print(0)
    elif person1 < person2:
        print(1)
    else:
        print(2)

main()
