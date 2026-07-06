"""Heron of Alexandria"""
import math
def main():
    """Heron of Alexandria"""
    a = float(input())
    b = float(input())
    c = float(input())
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    if (s - a) >= 0 and (s - b) >= 0 and (s-c) >= 0:
        print(f"{area:.3f}")
main()
