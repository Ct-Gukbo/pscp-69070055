"""ห้องเรียนและข้อความส่งต่อ"""


def main():
    """รับจำนวนนักเรียน จุดเริ่มต้น และกฎการส่งต่อ แล้วนับจำนวนผู้รับข้อความ"""
    n, s = map(int, input().split())
    forward = [0] * (n + 1)

    for i in range(1, n + 1):
        forward[i] = int(input())

    reached = [False] * (n + 1)
    current = s

    while True:
        reached[current] = True
        nxt = forward[current]

        if not nxt or reached[nxt]:
            break

        current = nxt

    print(sum(reached))
main()
