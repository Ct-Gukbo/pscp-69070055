"""Season"""
def main():
    """Season"""
    month = int(input())
    day = int(input())
    if (month in (1,2,3)):
        if day >= 21 and month == 3:
            print("spring")
        elif day <= 22 and month in (1,2,3):
            print("winter")
    elif (month in (4,5,6)):
        if day >= 21 and month == 6:
            print("summer")
        elif day <= 22 and month in (4,5,6):
            print("spring")
    elif (month in (7,8,9)):
        if day >= 21 and month == 9:
            print("fall")
        elif day <= 22 and month in (7,8,9):
            print("summer")
    elif (month in (10,11,12)):
        if day >= 21 and month == 12:
            print("winter")
        elif day <= 22 and month in (10,11,12):
            print("fall")
main()
