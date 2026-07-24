"""วันเกิด"""
def main():
    """วันเกิด"""
    y1 = int(input())
    m1 = int(input())
    d1 = int(input())
    y2 = int(input())
    m2 = int(input())
    d2 = int(input())
    person1 = ((2026-y1)*365)+(m1*30)+d1
    person2 = ((2026-y2)*365)+(m2*30)+d2
    if -7 <= person1 - person2 <= 7:
        print("0")
    elif person1 > person2:
        print("1")
    else:
        print("2")
main()
