"""กระดาษห่อของขวัญ"""
def main():
    """กระดาษห่อของขวัญ"""
    Number = input().split(" ")
    rad = float(Number[0])
    height = float(Number[1])
    distance = float(Number[2])
    radius = 2 * 3.14 * rad + distance
    print(f"{rad *2 + height:.2f}",f"{radius:.2f}")
main()
