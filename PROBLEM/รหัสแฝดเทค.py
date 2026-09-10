"""รหัสแฝดเทค"""
def main():
    """รหัสแฝดเทค"""
    n = int(input())
    a = input()
    b = input()

    wrong_count = 0
    for i in range(n):
        digit_a = int(a[i])
        digit_b = int(b[i])
        if digit_a + digit_b != 9:
            wrong_count += 1

    if not wrong_count :
        print("YES")
    else:
        print("NO", wrong_count)
main()
