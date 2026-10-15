"""สะสมเหรียญเวทย์มนตร์"""
def main():
    """ผลรวมของเหรียญ"""
    field_count = int(input())
    fire = 0
    water = 0
    earth = 0

    for _ in range(field_count):
        coins = list(map(int, input().split()))
        fire += max(coins[0], coins[3])
        water += max(coins[1], coins[4])
        earth += max(coins[2], coins[5])

    total = fire + water + earth
    bonus = "YES" if fire > water + earth else "NO"

    print(f"Total: {total}")
    print(f"Fire: {fire}")
    print(f"Water: {water}")
    print(f"Earth: {earth}")
    print(f"Bonus: {bonus}")

main()
