"""สลากกินแบ่ง"""
def main():
    """สลากกินแบ่ง"""
    code1 = input().strip()
    code2 = input().strip()

    if len(code1) < 2 or len(code2) < 2:
        print("0")
        return

    char1, num1 = code1[0], code1[1:]
    char2, num2 = code2[0], code2[1:]

    same_char = char1 == char2
    same_digits = num1 == num2
    last_3_match = (num1[-3:] == num2[-3:]) if len(num1) >= 3 and len(num2) >= 3 else False
    last_2_match = (num1[-2:] == num2[-2:]) if len(num1) >= 2 and len(num2) >= 2 else False

    if same_char and same_digits:
        print("1000000")
    elif not same_char and same_digits:
        print("100000")
    elif same_char and last_3_match:
        print("2000")
    elif not same_char and last_3_match:
        print("200")
    elif same_char and last_2_match:
        print("1000")
    elif not same_char and last_2_match:
        print("100")
    elif same_char:
        print("20")
    else:
        print("0")

main()
