"""SurprisingVote"""
def main():
    """SurprisingVote"""
    allscore = float(input())
    highest = float(input())
    function = allscore-highest
    lowest = max(0, function - highest)
    if (highest - lowest) > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
