"""BigFrame"""
def main():
    """BigFrame"""
    words = []
    for _ in range(5):
        words.append(input())

    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word

    width = len(longest)
    border = "*" * (width + 4)

    print(border)
    for word in words:
        print("*" + " " + word.ljust(width) + " " + "*")
    print(border)

main()
