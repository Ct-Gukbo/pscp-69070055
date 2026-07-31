"""Ticket"""
def main():
    """Ticket"""
    INPUT = input().split(" ")
    age =   int(INPUT[0])
    day = INPUT[1]
    if age < 5:
        print("0")
    elif age >= 19:
        print("150")
    elif day == "Wed":
        if age >= 19:
            print("75")
        else:
            print("50")
    else:
        print("100")
main()
