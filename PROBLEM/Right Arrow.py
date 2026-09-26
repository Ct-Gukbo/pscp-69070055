"""Right Arrow"""
def main():
    """Right Arrow"""
    k = int(input())
    h = int(input())
    middle = h // 2
    for i in range(middle):
        print(" " * i + "*" * k)
    print(" " * middle + "*" * k)
    for i in range(middle - 1, -1, -1):
        print(" " * i + "*" * k)
main()
