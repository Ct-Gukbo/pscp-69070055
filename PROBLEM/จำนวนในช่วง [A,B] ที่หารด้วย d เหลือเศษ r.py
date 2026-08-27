"""จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""
def main():
    """จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""
    A = int(input())
    B = int(input())
    d = int(input())
    r = int(input())
    if B < r:
        countB = 0
    else:
        countB = (B - r) // d + 1
    if (A - 1) < r:
        countA = 0
    else:
        countA = (A - 1 - r) // d + 1
    N = countB - countA
    print(N)
main()
