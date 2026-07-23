"""ค่าน้อยที่สุด"""
def main():
    """ค่าน้อยที่สุด"""
    a = int(input())
    b = int(input())
    c = int(input())
    if a <= b and a <= c:
        print(a)
    elif b <= a and b <= c:
        print(b)
    else:
        print(c)
main()
