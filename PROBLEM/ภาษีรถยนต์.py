"""ภาษีรถยนต์"""
def main():
    """ภาษีรถยนต์"""
    year = int(input())
    cc = int(input())

    if year <= 1990:
        if cc <= 1500:
            print(1250)
        elif cc > 2000:
            print(2000)
        else:
            print(1400)
    elif 1991 <= year <= 1999:
        if cc <= 1500:
            print(1100)
        elif cc >= 2000:
            print(1700)
        else:
            print(1300)
    else:
        if cc <= 1500:
            print(1000)
        elif cc >= 2000:
            print(1500)
        else:
            print(1200)
main()
