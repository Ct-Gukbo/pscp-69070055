"""Left Arrow"""
def main():
    """Left Arrow"""
    k = int(input())
    h = int(input())
    rows = h // 2
    for i in range(rows):
        print(" " * (rows-i) + "*" * k)

    print("*" * k)

    for i in range(rows):
        print(" " * (i+1) + "*" * k)
main()
