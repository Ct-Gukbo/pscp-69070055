"""กบน้อยกระโดด"""
def main():
    """กบน้อยกระโดด"""
    start, end = map(int, input().split())
    jump = 0
    count = 0
    while count < end and start > 0:
        count += start
        start -= 2
        jump += 1
    if count >= end:
        print(jump)
    else:
        print("-1")
main()
