"""Calculator"""
def main():
    """Calculator"""
    Time = int(input())
    if Time  == 1 :
        print(Time)
    else :
        for i in range(1, Time + 1):
            Time += len(str(i))
        print(Time)
main()
