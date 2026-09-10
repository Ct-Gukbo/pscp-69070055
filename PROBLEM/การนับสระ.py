"""การนับสระ"""
def main():
    """การนับสระ"""
    word = input()
    Vowel = ["a", "e", "i", "o", "u"]
    count = 0
    for i in word:
        if i in Vowel:
            count += 1
    print(count)
main()
