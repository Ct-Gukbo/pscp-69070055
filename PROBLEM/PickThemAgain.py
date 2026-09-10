"""PickThemAgain"""
def main():
    """PickThemAgain"""
    input_list = [int(x) for x in input().split()]
    found = False
    for _, num in reversed(list(enumerate(input_list))):
        if not num % 3 or not num % 5:
            print(num)
            found = True
    if not found:
        print("Nope")
main()
