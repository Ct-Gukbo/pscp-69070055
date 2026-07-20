"""Temperature"""

def main():
    """Temperature"""
    value = float(input())
    in_unit = input()
    out_unit = input()

    if in_unit == "C":
        c = value
    elif in_unit == "K":
        c = value - 273.15
    elif in_unit == "F":
        c = (value - 32) * 5 / 9
    else:
        c = value * 5 / 9 - 273.15

    if out_unit == "C":
        ans = c
    elif out_unit == "K":
        ans = c + 273.15
    elif out_unit == "F":
        ans = c * 9 / 5 + 32
    else:
        ans = (c + 273.15) * 9 / 5

    print(f"{ans:.2f}")

main()
