"""Factorial"""
def main():
    """Factorial"""
    num = int(input())
    answer = 1
    for _ in range(1, num+1):
        answer *= _
    print(answer)
main()
