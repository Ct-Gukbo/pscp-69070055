"""3 เหลี่ยม"""
def main():
    """3 เหลี่ยม"""
    row = int(input())
    for _ in range (row):
        if not _ :
            print("0")
        elif _ == 1:
            print("00")
        elif _ == row - 1:
            print("0" * row)
        else:
            print("0" + "1" * (_ - 1) + "0")
main()
