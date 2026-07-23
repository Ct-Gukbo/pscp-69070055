"""Season"""
def main():
    """Season"""
    month = int(input())
    day = int(input())
    if month in (1, 2, 3):
        if month == 3 and day >= 21:
            print("spring")
        else:
            print("winter")
    elif month in (4, 5, 6):
        if day >= 21 and month == 6:
            print("summer")
        else:
            print("spring")
    elif month in (7, 8, 9):
        if day >= 21 and month == 9:
            print("fall")
        else:
            print("summer")
    elif month in (10, 11, 12):
        if day >= 21 and month == 12:
            print("winter")
        else:
            print("fall")
main()
