"""Ink"""
import math
def main():
    """Ink"""
    AreaPerSecond , n = map(int , input().split())

    for _ in range(n):
        x , y = map(int , input().split())
        Radius = x**2 + y**2
        Radius = math.sqrt(Radius)
        Area = 3.1416 * (Radius ** 2)
        Second = Area / AreaPerSecond

        print(math.ceil(Second))
main()
