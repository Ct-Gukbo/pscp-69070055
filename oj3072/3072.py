"""aeiou"""
def main():
    """aeiou"""
    vowel  = ["a", "e", "i", "o", "u"]
    vowel_count = [0, 0, 0, 0, 0]
    text = input().lower()
    for _ in text:
        if _ == "a":
            vowel_count[0] += 1
        elif _ == "e":
            vowel_count[1] += 1
        elif _ == "i":
            vowel_count[2] += 1
        elif _ == "o":
            vowel_count[3] += 1
        elif _ == "u":
            vowel_count[4] += 1
    for _ in range(5):
        if vowel_count[_] > 0:
            print(vowel[_], ":", vowel_count[_])
main()
