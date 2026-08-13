"""ปราสาท"""
def main():
    """ปราสาท"""
    num = int(input())
    i = 1
    j = 0
    count = 0
    # 2^2 3^2 4^2 5^2
    while j < num:
        count += 1
        i += 1
        j = i**2
    ans = count*2
    if num == 1:
        print("0")
    elif not j % 2:
        if not num % 2 :
            print(ans)
        else:
            print(ans-1)
    else:
        if not num % 2 :
            print(ans-1)
        else:
            print(ans)
main()
