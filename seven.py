"""seven"""
def main():
    """seven"""
    sev = int(input())

    if not sev:
        print(1)
    else:
        last_digit = [7, 9, 3, 1]
        print(last_digit[(sev - 1) % 4])

main()
