"""วันแรกที่วิ่งถึงเป้าหมาย"""
import sys

def main():
    """วันแรกที่วิ่งถึงเป้าหมาย"""
    data = sys.stdin.read().split()
    n, t = int(data[0]), int(data[1])
    total = 0
    for i in range(n):
        total += int(data[2 + i])
        if total >= t:
            print(i + 1)
            return
    print(-1)

main()
