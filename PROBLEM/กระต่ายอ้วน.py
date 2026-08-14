"""กระต่ายอ้วน"""
def main():
    """กระต่ายอ้วน"""
    bunny = int(input())
    i = 0
    savename = ""
    save = 0
    for _ in range(bunny):
        Name , Weight  = input().split()
        if int(Weight) > 15:
            i += 1
        if int(Weight) > save :
            save = int(Weight)
            savename = Name
    print(i)
    print(savename)
main()
