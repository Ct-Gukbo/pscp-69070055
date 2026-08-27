"""สหกรณ์โรงเรียน"""
from decimal import Decimal, ROUND_HALF_UP
def main():
    """สหกรณ์โรงเรียน"""
    Pass = input().strip()
    Count = int(input())
    totalprice = Decimal("0")
    for _ in range(Count):
        price = Decimal(input().strip())
        totalprice += price
    if Pass == "Y":
        totalprice = totalprice * Decimal("0.95")
    elif Pass == "N" and totalprice >= 500:
        totalprice = totalprice * Decimal("0.97")
    result = totalprice.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    print(f"{result:.2f}")
main()#i use ai by check the test case and find a way to round up best
