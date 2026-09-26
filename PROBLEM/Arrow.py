"""Arrow"""
def arrow_r(counte):
    """Right arrow"""
    lines = []
    for i in range(counte):
        lines.append(" " * (i * 2) + "*" * (counte - i))
    for i in range(counte - 1):
        lines.append(" " * ((counte - (i + 2)) * 2) + "*" * (i + 2))
    return lines

def arrow_l(counte):
    """Left arrow"""
    lines = []
    for i in range(counte):
        lines.append(" " * (counte - (i + 1)) + "*" * (counte - i))
    for i in range(counte - 1):
        lines.append(" " * (i + 1) + "*" * (i + 2))
    return lines

def main():
    """Arrow"""
    keyword = input()
    counte = int(input())
    lines = []
    prev = ""
    for ch in keyword:
        if ch not in "RL":
            continue
        if prev:
            lines.append("")
        lines.extend(arrow_r(counte) if ch == "R" else arrow_l(counte))
        prev = ch
    print("\n".join(lines), end="")
main()
