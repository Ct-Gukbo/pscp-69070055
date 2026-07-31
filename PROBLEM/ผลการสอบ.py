"""ผลการสอบ"""
def main():
    """ผลการสอบ"""
    HW = int(input())
    MT = int(input())
    FN = int(input())
    if HW >= 5 and MT >= 20 and FN >=25:
        print("pass")
    else:
        print("fail")
main()
