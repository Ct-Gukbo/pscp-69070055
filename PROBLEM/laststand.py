"""last stand"""
text = input()

text = text.replace("[", " ")
text = text.replace("]", " ")
text = text.replace(",", " ")

numbers = text.split()

for x in numbers:
    n = int(x)
    print(n % 10)
