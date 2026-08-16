"""ราศี"""
def main():
    """ราศี"""
    day = int(input())
    month = int(input())

    zodiac = {
        1: "capricorn",
        2: "aquarius",
        3: "pisces",
        4: "aries",
        5: "taurus",
        6: "gemini",
        7: "cancer",
        8: "leo",
        9: "virgo",
        10: "libra",
        11: "scorpio",
        12: "sagittarius"
    }
    limit = {
        1: 19,
        2: 18,
        3: 20,
        4: 19,
        5: 20,
        6: 21,
        7: 22,
        8: 22,
        9: 22,
        10: 23,
        11: 21,
        12: 21
    }
    if day <= limit[month]:
        print(zodiac[month])
    elif month == 12:
        print(zodiac[1])
    else:
        print(zodiac[month + 1])
main()
