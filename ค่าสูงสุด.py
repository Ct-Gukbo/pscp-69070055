"""ค่าสูงสุด"""
def main():
    """ค่าสูงสุด"""
    a = int(input())
    b = int(input())
    c = int(input())
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > a and c > b:
        print(c)
    elif a == b > c:
        print(a,b)
    elif b == c > a:
        print(b,c)
    elif c == a > b:
        print(a,c)
    else :
        print(a,b,c)
main()
