"""เกมทายลูกเต๋า"""
def main():
    """เกมทายลูกเต๋า"""
    first = int(input())
    second = int(input())
    if 1 <= first <= 6 and 1 <= second <= 6:
        if first == second:
            print("Correct!")
        else:
            print("Wrong!")
    else:
        print("Invalid")
main()
