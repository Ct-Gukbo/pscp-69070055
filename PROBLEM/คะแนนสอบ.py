"""คะแนนสอบ"""
def main():
    """คะแนนสอบ"""
    Number = int(input())
    Score = [int(input()) for i in range(Number)]
    highest = max(Score)
    print(highest)
    total = Score.count(highest)
    print(total)
main()
