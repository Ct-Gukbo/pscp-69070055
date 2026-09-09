"""Conan"""
def main():
    """Conan"""
    Word = input()
    Num = int(input())
    Final = ""
    for _ in Word:
        Final += chr((ord(_) - ord('a') + Num) % 26 +ord('a'))
    print(Final)
main()
