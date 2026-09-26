"""แปลงดอกไม้"""
def main():
    """แปลงดอกไม้"""
    L, N = map(int, input().split())

    count = 0
    band = 0

    while count < N:
        size = L * L * band + L * (L + 1) // 2
        count = count + size
        band = band + 1

    print(band)
main()
