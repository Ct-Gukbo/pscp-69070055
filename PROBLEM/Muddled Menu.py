"""Muddled Menu"""

menu = []

while True:
    line = input().strip()

    if line == "CLOSED":
        menu = []
        break

    if line == "SOMETHING'S WRONG":
        menu = []
        continue

    if line.startswith("Can't do: "):
        food = line.replace("Can't do: ", "")
        if food in menu:
            menu.remove(food)
        continue

    if line == "DONE":
        break

    name, tag = line.split("#")
    name = name.strip()
    tag = tag.strip()

    if tag == "N":
        menu.append(name)
    else:
        pos = int(tag)
        if pos <= 0:
            pos = 1
        if pos > len(menu) + 1:
            pos = len(menu) + 1
        menu.insert(pos - 1, name)

print("Full Course:", menu, "Reversed:", menu[::-1])
