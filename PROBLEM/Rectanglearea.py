"""rectangle area"""
def main():
    """rectangle area"""
    rec1 = (input().split(" "))
    rec2 = (input().split(" "))
    x1 = int(rec1[0])
    y1 = int(rec1[1])
    width = int(rec1[2])
    height = int(rec1[3])
    x2 = int(rec2[0])
    y2 = int(rec2[1])
    width2 = int(rec2[2])
    height2 = int(rec2[3])
    x = max(0, min(x1+width, x2+width2) - max(x1, x2))
    y = max(0, min(y1+height, y2+height2) - max(y1, y2))
    area = x*y
    if  area > 0:
        print(area)
    else:
        print("no overlapping")
main()
