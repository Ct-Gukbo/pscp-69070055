"""บุพเพสันนิวาส"""

name1 = input()
name2 = input()

while len(name1) < len(name2):
    name1 = name1 + name1[0]

while len(name2) < len(name1):
    name2 = name2 + name2[0]

love_letters = {'l', 'L', 'o', 'O', 'v', 'V', 'e', 'E'}

yantra = ""

for i, (c1, c2) in enumerate(zip(name1, name2)):

    if c1 in love_letters or c2 in love_letters:
        yantra += 'w'
    else:
        yantra += '$'

w_count = 0
for c in yantra:
    if c == 'w':
        w_count += 1

max_consecutive = 0
current_streak = 0

for c in yantra:
    if c == 'w':
        current_streak += 1
        if current_streak > max_consecutive:
            max_consecutive = current_streak
    else:
        current_streak = 0

has_consecutive_w = False
for i in range(len(yantra) - 1):
    if yantra[i] == 'w' and yantra[i + 1] == 'w':
        has_consecutive_w = True
        break

if w_count % 2 == 1:
    yantra += str(max_consecutive)
else:

    if not has_consecutive_w:
        yantra += '#'

print(yantra)
