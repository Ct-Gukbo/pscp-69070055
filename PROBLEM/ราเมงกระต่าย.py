"""ราเมงกระต่าย"""
def main():
    """ราเมงกระต่าย"""
    price = {
        ('S', 'R'): 60, ('S', 'T'): 80,
        ('M', 'R'): 80, ('M', 'T'): 100,
        ('L', 'R'): 100, ('L', 'T'): 120,
    }
    size, suid = input().split()
    total = price[(size, suid)]
    topping = input().split()
    if topping[0] != 'N':
        kind = topping[0]
        count = int(topping[1])
        if kind == 'P':
            total += 15 * count
        elif kind == 'E':
            total += 10 * count
    print(total)
main()
