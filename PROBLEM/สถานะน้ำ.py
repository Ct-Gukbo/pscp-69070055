"""สถานะน้ำ"""
def main():
    """สถานะน้ำ"""
    temparature = int(input())
    variable = str(input().lower())
    if variable == "c":
        if temparature >= 100:
            print("gas")
        elif temparature <= 0:
            print("solid")
        else:
            print("liquid")
    elif variable == "f":
        if temparature >= 212:
            print("gas")
        elif temparature <= 32:
            print("solid")
        else:
            print("liquid")
main()
