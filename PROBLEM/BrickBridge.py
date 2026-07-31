"""BrickBridge"""
def main():
    """BrickBridge"""
    smallbrick = int(input())
    bbrick = int(input())
    goal = int(input())
    bigbrick = bbrick*5
    count = 0
    for i in range(goal):
        goal -= bigbrick
        count += 1
        goal -= smallbrick
        count += 1
        print(count)
    if bigbrick + smallbrick < goal:
        print("-1")
    else:
        print(count)
main()
