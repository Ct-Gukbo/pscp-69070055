"""Heron of Alexandria"""
import math
def main():
    """Heron of Alexandria"""
    a = int(input())
    b = int(input())
    c = int(input())
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    if (s - a) >= 0 and (s - b) >= 0 and (s-c) >= 0:
        print(f"{area:.3f}")
    else:
        return
main()
