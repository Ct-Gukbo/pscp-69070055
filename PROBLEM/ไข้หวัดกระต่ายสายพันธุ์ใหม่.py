"""ไข้หวัดกระต่ายสายพันธุ์ใหม่"""
rows, cols = map(int, input().split())

rabbit_row, rabbit_col = map(int, input().split())

n = int(input())

grid = []
for _ in range(rows):
    grid.append([0] * cols)

for _ in range(n):
    inf_r, inf_c = map(int, input().split())

    for r in range(3):
        risk = 0
        if not r:
            risk = 100
        elif r == 1:
            risk = 60
        else:
            risk = 20
        for i in range(max(0, inf_r - r), min(rows, inf_r + r + 1)):
            for j in range(max(0, inf_c - r), min(cols, inf_c + r + 1)):

                dist = max(abs(i - inf_r), abs(j - inf_c))
                if dist == r:
                    if risk > grid[i][j]:
                        grid[i][j] = risk

safe_count = 0
for i in range(rows):
    for j in range(cols):
        if not grid[i][j]:
            safe_count += 1


rabbit_risk = grid[rabbit_row][rabbit_col]

print(safe_count)
if not rabbit_risk:
    print("0%")
elif rabbit_risk == 20:
    print("20%")
elif rabbit_risk == 60:
    print("60%")
else:
    print("100%")
