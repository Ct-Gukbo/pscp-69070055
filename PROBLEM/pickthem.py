"""Pick Them"""
line = input()

line = line.replace('[', '').replace(']', '')
parts = line.split(',')
numbers = []
for part in parts:
    n = int(part.strip())
    numbers.append(n)

evens = []
for n in numbers:
    if not n % 2:
        evens.append(n)

if not evens:
    print("Nope")
else:
    for n in evens:
        print(n)
