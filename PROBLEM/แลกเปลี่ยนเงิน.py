"""แลกเปลี่ยนเงิน"""
def main():
    """แลกเปลี่ยนเงิน"""
    money = int(input())
    ten = money // 10
    five = (money - ten * 10) // 5
    two = (money - ten * 10 - five * 5) // 2
    one = money - ten * 10 - five * 5 - two * 2
    print("10 = " + str(ten))
    print("5 = " + str(five))
    print("2 = " + str(two))
    print("1 = " + str(one))
main()
