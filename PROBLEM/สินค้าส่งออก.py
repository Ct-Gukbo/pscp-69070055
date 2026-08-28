"""สินค้าส่งออก"""
def main():
    """สินค้าส่งออก"""
    n = int(input())
    SUM = 0
    EVEN = 0
    ODD = 0
    for _ in range(n):
        Input = int(input())
        SUM += Input
        if not Input % 2:
            EVEN += 1
        else:
            ODD += 1
    print(f"SUM {SUM}")
    print(f"EVEN {EVEN}")
    print(f"ODD {ODD}")
main()
