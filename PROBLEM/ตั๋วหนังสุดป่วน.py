"""ตั๋วหนังสุดป่วน"""
def main():
    """ตั๋วหนังสุดป่วน"""
n = int(input())

while True:
    line = input()
    if not line:
        break

    age, tickets = line.split()
    age = int(age)
    tickets = int(tickets)

    if age < 15:
        print(-1)
    elif tickets > n:
        print(-2)
    else:
        price = 150

        if 15 <= age <= 22:
            price = 150 * 0.8
        elif age >= 60:
            price = 150 * 0.5

        total = price * tickets
        n = n - tickets
        print(int(total), n)

    if n <= 0:
        break
main()
