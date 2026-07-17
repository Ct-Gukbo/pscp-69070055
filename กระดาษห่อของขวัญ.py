"""กระดาษห่อของขวัญ"""
def main():
    """กระดาษห่อของขวัญ"""
    Number = input().split(" ")
    rad = int(Number[0])
    height = int(Number[1])
    distance = int(Number[2])
    radius = 2 * 3.14 * rad
    print(f"{radius}.2f")
    
main()