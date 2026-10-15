"""Day08-0_02-Backward"""
lines = []

while True:
    line = input()
    if line == "NULL":
        break
    lines.append(line)

i = len(lines) - 1
while i >= 0:
    print(lines[i])
    i = i - 1
