"""Smart Trash Collector"""
n = int(input())

for _ in range(n):
    line = input()
    parts = line.split(' ')

    plastic = float(parts[0])
    can = float(parts[1])
    glass = float(parts[2])

    total = plastic + can + glass

    messages = []

    if total > 50.0:
        messages.append("Overloaded")

    if plastic > 20.0:
        messages.append("Check Type Plastic")

    if can > 20.0:
        messages.append("Check Type Can")

    if glass > 20.0:
        messages.append("Check Type Glass")

    if not messages:
        print(f"{total:.1f}")
    else:
        output = f"{total:.1f}"
        for msg in messages:
            output = output + ", " + msg
        print(output)
