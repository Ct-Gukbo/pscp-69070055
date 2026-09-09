"""ผ่านหรือไม่ ค่าเฉลี่ยรายวิชา"""
def main():
    """ผ่านหรือไม่ ค่าเฉลี่ยรายวิชา"""
    Count = int(input())
    Sum = 0
    score = []
    for _ in range(Count):
        Num = int(input())
        score.append(Num)
    Average = sum(score) / Count
    print(f"{Average:.1f}")
    if min(score) >= 50.0 and Average >= 60.0:
        print("PASS")
    else:
        print("FAIL")
main()
