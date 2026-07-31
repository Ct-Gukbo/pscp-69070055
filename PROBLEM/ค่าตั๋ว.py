"""ค่าตั๋ว"""
def main():
    """ค่าตั๋ว"""
    age = int(input())
    stu = str(input().lower())
    if age < 18 or stu == "s":
        print("20")
    else:
        print("50")
main()
