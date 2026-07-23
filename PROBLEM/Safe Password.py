"""Safe Password"""
def main():
    """Safe Password"""
    character = (str(input()))
    code = (str(input()))
    if character == "H" and code == "4567" :
        print("safe unlocked")
    elif character == "H" and code != "4567" :
        print("safe locked - change digit")
    elif character != "H" and code == "4567" :
        print("safe locked - change char")
    else :
        print("safe locked")
main()
