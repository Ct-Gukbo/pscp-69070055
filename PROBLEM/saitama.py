"""saitama"""
def main():
    """saitama"""
    push = int(input())
    sit = int(input())
    stand = int(input())
    run = int(input())
    push1 = int(input())
    sit1 = int(input())
    run1 = int(input())
    stand1 = int(input())
    day_push = (push + push1 - 1) // push1
    day_sit = (sit + sit1 - 1) // sit1
    day_stand = (stand + stand1 - 1) // stand1
    day_run = (run + run1 - 1) // run1
    print(max(day_push, day_sit, day_stand, day_run))
main()
