"""หั่นขนมปัง"""
w, h, m, n = map(int, input().split())

x_cuts = list(map(int, input().split()))
y_cuts = list(map(int, input().split()))

assert len(x_cuts) == m, "Expected m vertical cuts"
assert len(y_cuts) == n, "Expected n horizontal cuts"

v_widths = []
prev = 0
for x in x_cuts:
    v_widths.append(x - prev)
    prev = x
v_widths.append(w - prev)

h_heights = []
prev = 0
for y in y_cuts:
    h_heights.append(y - prev)
    prev = y
h_heights.append(h - prev)

max_w1 = 0
max_w2 = 0
for width in v_widths:
    if width > max_w1:
        max_w2 = max_w1
        max_w1 = width
    elif width > max_w2:
        max_w2 = width

max_h1 = 0
max_h2 = 0
for height in h_heights:
    if height > max_h1:
        max_h2 = max_h1
        max_h1 = height
    elif height > max_h2:
        max_h2 = height

area1 = max_w1 * max_h1
area2 = max(max_w1 * max_h2, max_w2 * max_h1)

print(area1, area2)
