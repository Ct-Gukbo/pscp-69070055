"""เกมสะสมแต้ม"""
def main():
    """เกมสะสมแต้ม"""
    Many = int(input())
    total = 0
    for _ in range(Many):
        score = str(input())
        if score == "+":
            total += 10
        else:
            total -= 5
    print(total)
main()
