"""วาด X-shape"""
def main():
    """วาด X-shape"""
    x, k = input().split()
    x = int(x)
    mid = x // 2
    for i in range(x):
        row = ""
        for j in range(x):
            if j in (i, x - 1 - i):
                d = abs (i - mid)
                if k == '#':
                    row += '#'
                else:
                    row += chr(ord(k) + d)
            else:
                row += '-'
        print(row)
main()
