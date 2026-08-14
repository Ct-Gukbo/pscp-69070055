"""coke"""
def main():
    """coke"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    if not b:
        print(a * d)
    elif not d :
        print(0)
    else:
        n_pro = (d-1) // b
        n_base = d - n_pro
        price = (n_pro * c) + (n_base * a)
        print(price)
main()
