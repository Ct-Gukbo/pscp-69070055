"""ฟิลเตอร์ AR TikTok"""
def main():
    """ฟิลเตอร์ AR TikTok"""
    Number = input().split(" ")
    r = int(Number[0])
    x = int(Number[1])
    y = int(Number[2])
    R = x**2 + y**2
    if r**2 > R:
        print("IN")
    elif r**2 == R:
        print("ON")
    elif r**2 < R:
        print("OUT")
main()
