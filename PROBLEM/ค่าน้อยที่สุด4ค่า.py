"""ค่าน้อยที่สุด4ค่า"""
def main():
    """ค่าน้อยที่สุด4ค่า"""
    INPUT = int(input())

    smallest = int(input())

    for _ in range(INPUT - 1):
        num = int(input())
        if num < smallest:
            smallest = num

    print(smallest)
main()
