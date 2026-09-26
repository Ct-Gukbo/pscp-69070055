"""หาจำนวนเฉพาะ"""
def main():
    """หาจำนวนเฉพาะ"""
    first, last = map(int, input().split(" "))
    primes = []
    for _ in range(first, last + 1):
        if _ > 1:
            for i in range(2, _):
                if not _ % i:
                    break
            else:
                primes.append(str(_))
    if not primes:
        print("Total primes: 0")
    else:
        print(" ".join(primes))
        print(f"Total primes: {len(primes)}")
main()
