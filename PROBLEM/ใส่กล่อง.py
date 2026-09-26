"""ใส่กล่อง"""
def main():
    """ใส่กล่อง"""
    W, L, M, N = map(int, input().split())

    best = -1

    for A in range(M, N + 1):
        r1 = W % A
        r2 = L % A
        waste = r1 * r2

        if best == -1 or waste < best:
            best = waste

    print(best)
main()
