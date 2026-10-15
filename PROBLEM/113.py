"""113"""
line = input()

while True:
    found = False
    for i in range(len(line) - 2):
        if line[i] == '1' and line[i+1] == '1' and line[i+2] == '3':
            line = line[:i] + line[i+3:]
            found = True
            break

    if not found:
        break

print(line)
