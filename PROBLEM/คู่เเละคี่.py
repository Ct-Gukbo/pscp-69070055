"""even and odd"""
def main():
    """even and odd"""
    first = int(input())
    second = int(input())
    third = int(input())
    odd = 0
    even = 0
    if not first % 2:
        even += 1
    if not second % 2:
        even += 1
    if not third % 2:
        even += 1
    if first % 2 :
        odd += 1
    if second % 2 :
        odd += 1
    if third % 2 :
        odd += 1
    print(even)
    print(odd)
main()
