"""stats"""
def main():
    """stats"""
    row = int(input())
    presetmax = -100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    presetmin = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    presetavg = 0
    if row >= 0:
        for _ in range(row):
            variable = int(input())
            if variable >= presetmax:
                presetmax = variable
            if variable <= presetmin:
                presetmin = variable
            presetavg += variable
        AVG = presetavg / row
        print("MIN:",f"{presetmin:.3f}")
        print("MAX:",f"{presetmax:.3f}")
        print("AVG:",f"{AVG:.3f}")
main()