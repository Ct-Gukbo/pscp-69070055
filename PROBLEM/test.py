"""coke"""
def main():
    """coke"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    sumcap = 0
    sumcost = 0
    for _ in range(d):
        if 0 < b < sumcap:
            sumcost += c
            sumcap -= b
        else:
            sumcost += a
        sumcap += 1
    print(sumcost)
main()