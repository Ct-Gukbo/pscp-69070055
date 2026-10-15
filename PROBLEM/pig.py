"""pig"""
n = int(input())
w = input().split()

bigs = []
total = 0

for i in range(n):
    a = int(w[2 * i])
    b = int(w[2 * i + 1])
    if a > b:
        big = a
    else:
        big = b
    bigs.append(big)
    total = total + big

if n == 1:
    print(total)
else:
    equation = ""
    for i, big in enumerate(bigs):
        if i > 0:
            equation = equation + " + "
        equation = equation + str(big)
    print(equation + " = " + str(total))
