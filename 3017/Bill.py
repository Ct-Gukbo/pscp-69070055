"""Bill"""
def main():
    """Bill"""
    price = int(input())
    price_bori = price * 0.1
    if price_bori <= 50:
        price_bori = 50
    elif price_bori >= 1000:
        price_bori = 1000
    price_vat = (price_bori + price)*1.07
    print(f"{price_vat:.2f}")
main()
