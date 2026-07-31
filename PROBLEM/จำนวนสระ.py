"""จำนวนสระ"""
def main():
    """จำนวนสระ"""
    times = int(input())
    i = 0
    for _ in range(times):
        alphabet = str(input())
        if alphabet in ("A","E","I","O","U"):
            i += 1
    print(i)
main()
