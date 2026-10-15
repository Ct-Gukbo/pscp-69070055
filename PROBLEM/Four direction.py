"""four direction"""
up = ["  *  ", " *** ", "* * *", "  *  ", "  *  "]
down = ["  *  ", "  *  ", "* * *", " *** ", "  *  "]
left = ["  *  ", " *   ", "*****", " *   ", "  *  "]
right = ["  *  ", "   * ", "*****", "   * ", "  *  "]

text = input()

for row in range(5):
    line = ""
    for ch in text:
        if ch == "U":
            line = line + up[row] + " "
        if ch == "D":
            line = line + down[row] + " "
        if ch == "L":
            line = line + left[row] + " "
        if ch == "R":
            line = line + right[row] + " "
    print(line)
