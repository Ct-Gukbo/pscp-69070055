"""โรงแรมกลางกรุง ไม่มีชั้น 13"""
def main():
    """โรงแรมกลางกรุง ไม่มีชั้น 13"""
    raw_input = input().strip().zfill(5)
    d = [int(ch) for ch in raw_input]
    floors = ["9", "10", "11", "12", "14"]
    first_part = "13"
    for i in range(5):
        if d[i] > 5:
            first_part = floors[i]
            break
    is_pal = d == d[::-1]
    c1 = (d[0] + d[4] > 5) if is_pal else (bool(d[4]) and d[0] // d[4] > 5)
    c2 = (d[1] * d[3] > 5) if is_pal else (d[1] - d[4] > 5)
    if c1:
        second_part = "1"
    elif c2:
        second_part = "2"
    else:
        second_part = "0"
    prod = d[0] * d[1] * d[2] * d[3] * d[4]
    if sum(d) > 25:
        third_part = "1"
    elif prod > 55:
        third_part = "2"
    else:
        third_part = "0"
    print(f"{first_part}{second_part}{third_part}")
main()
