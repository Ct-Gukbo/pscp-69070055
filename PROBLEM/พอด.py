"""พอด"""
def main():
    """พอด"""
    pod = input().split(" ")
    person = int(pod[0])
    row = int(pod[1])
    Person = []
    Row = []
    for _ in range(row):
        Row.append(int(_+1))
    for _ in range(person):
        inrow = int(input())
        Person.append(inrow)
    Count = [Person.count(n) for n in Row]
    total = sum(Count)
    Remain = total - row*min(Count)
    print(Remain)
main()
