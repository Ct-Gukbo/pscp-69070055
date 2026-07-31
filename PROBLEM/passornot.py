"""ผ่าน/ไม่ผ่าน"""
def main():
    """ผ่าน/ไม่ผ่าน"""
    int1 = int(input())
    int2 = int(input())
    final = int1 + int2
    print(final)
    if final >= 50:
        print("pass")
    else:
        print("fail")
main()
