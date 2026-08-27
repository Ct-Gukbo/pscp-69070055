"""ASCII"""
def main():
    """ASCII"""
    school = input()
    first = ord(school[0])
    last = ord(school[-1])
    length = len(school)
    result = []
    for i in range(10):
        digit = i
        if (i + 1) % 2 == 1:
            value = first + digit
        else:
            value = last - digit
        value %= length
        value %= 10
        result.append(value)
    print(result)
main()