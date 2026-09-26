"""Teaching schedule."""
def main():
    """Calculate and format teaching schedule time."""
    day = int(input())
    hr = int(input())
    alltime = day * hr

    if not alltime:
        print("No teaching")
        return

    hour = alltime // 60
    minute = alltime - (hour * 60)

    if not minute:
        print(f"{hour} hours")
    elif not hour:
        print(f"{minute} minute")
    else:
        print(f"{hour} hours {minute} minute")
main()
