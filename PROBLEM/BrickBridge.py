"""BrickBridge"""
def main():
    """BrickBridge"""
    smallbrick = int(input())
    bbrick = int(input())
    goal = int(input())
    big = min(bbrick,goal // 5)
    left = goal - (big * 5)
    if bbrick >= big:
        if smallbrick >= left:
            print(left)
        else:
            print(-1)
    else:
        print(-1)
main()
