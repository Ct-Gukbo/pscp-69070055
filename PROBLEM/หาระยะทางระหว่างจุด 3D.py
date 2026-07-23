"""หาระยะทางระหว่างจุด 3D"""
import math
first = input().split(" ")
second = input().split(" ")
x1 = int(first[0])
y1 = int(first[1])
z1 = int(first[2])
x2 = int(second[0])
y2 = int(second[1])
z2 = int(second[2])
answer = math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
print(f"{answer:.2f}")
