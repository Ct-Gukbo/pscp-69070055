"""4เหลี่ยม"""
def main():
    """4เหลี่ยม"""
    row = int(input())
    for _ in range (row):
        if not _:
            print("0"*row)
        elif _ == row - 1:
            print("0"*row)
        else:
            print("0" + "1" * (row - 2) + "0")
main()