"""หาร 10"""
def main():
    """หาร 10"""
    IN = int(input())
    ans = IN - (IN % 10)
    while ans >= 0:
        print(ans, end=" ")
        ans -= 10
main()
