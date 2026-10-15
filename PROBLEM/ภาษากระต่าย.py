"""ภาษากระต่าย"""
def check_word(word):
    """ภาษากระต่าย"""
    word = word.strip().upper()
    previous_char = ""

    for index, char in enumerate(word):
        if char not in ("R", "A", "B", "I", "T"):
            return "no", index
        if previous_char == "R" and char != "A":
            return "no", index
        if previous_char == "B" and char not in ("I", "T"):
            return "no", index
        if char == "A" and previous_char not in ("R", "A"):
            return "no", index
        previous_char = char

    if previous_char in ("R", "B"):
        return "no", len(word)

    if all(char in ("I", "T") for char in word):
        return "unknown", len(word)

    longest = 0
    current = 0
    for char in word:
        if char == "A":
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return "yes", longest


def main():
    """ภาษากระต่าย"""
    word = input()
    status, number = check_word(word)
    print(status, number)


main()
