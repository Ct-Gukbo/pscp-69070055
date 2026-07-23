"""หารลงตัว"""
def main():
    """หารลงตัว"""
    IN = int(input())
    div = int(input())
    if not IN % div:
        print("yes")
    else:
        print("no")
main()
