"""Milk"""
def main():
    """Milk"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    milk = d // a
    if b:
        caps = milk
        while caps >= b:
            new_milk = (caps // b) * c
            milk += new_milk
            caps = caps % b + new_milk
    print(milk)
main()
