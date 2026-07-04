"""Cyan's password generator"""
def main():
    """Cyan's password generator"""
    NAME = str(input())
    SURNAME = str(input())
    AGE = int(input())
    if len(NAME) >= 5 and len(SURNAME) >= 5:
        print(NAME[0:2] + SURNAME[:-2:-1] + str(AGE)[:-2:-1] )
    else :
        print(NAME[0:1] + str(AGE) + SURNAME[:-2:-1])
main()
