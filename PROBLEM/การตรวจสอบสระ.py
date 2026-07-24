"""การตรวจสอบสระ"""
def main():
    """การตรวจสอบสระ"""
    alphabet = str(input().lower())
    if alphabet in ("a","e","i","o","u"):
        print("yes")
    else:
        print("no")
main()
