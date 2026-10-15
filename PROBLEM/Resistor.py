"""Resistor"""


def main():
    """Resistor"""
    colors = [input().strip() for _ in range(4)]

    digit_color = {
        "Black": 0,
        "Brown": 1,
        "Red": 2,
        "Orange": 3,
        "Yellow": 4,
        "Green": 5,
        "Blue": 6,
        "Purple": 7,
        "Grey": 8,
        "White": 9,
    }

    multiplier_color = {
        "Black": 1,
        "Brown": 10,
        "Red": 100,
        "Orange": 1000,
        "Yellow": 10000,
        "Green": 100000,
        "Blue": 1000000,
        "Purple": 10000000,
        "Gold": 0.1,
        "Silver": 0.01,
    }

    tolerance_color = {
        "Brown": 1,
        "Red": 2,
        "Green": 0.5,
        "Blue": 0.25,
        "Purple": 0.10,
        "Grey": 0.05,
        "Gold": 5,
        "Silver": 10,
    }

    if len(colors) != 4:
        print("Error")
        return

    first, second, multiplier_name, tolerance_name = colors

    if (
        first not in digit_color
        or second not in digit_color
        or multiplier_name not in multiplier_color
        or tolerance_name not in tolerance_color
    ):
        print("Error")
        return

    base = digit_color[first] * 10 + digit_color[second]
    multiplier = multiplier_color[multiplier_name]
    tolerance = tolerance_color[tolerance_name]

    nominal = base * multiplier
    lower = nominal - nominal * tolerance / 100
    upper = nominal + nominal * tolerance / 100

    print(f"{lower:.4f}")
    print(f"{upper:.4f}")

main()
