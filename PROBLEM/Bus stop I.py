"""Bus stop I"""
def main():
    """Bus stop I"""
    capacity = int(input())
    stop_count = int(input())

    waiting = {}
    for _ in range(stop_count):
        data = list(map(int, input().split()))
        waiting[data[0]] = data[1:]

    bus = []
    delivered = 0

    for stop in range(1, stop_count + 1):
        delivered += bus.count(stop)
        bus = [dest for dest in bus if dest != stop]

        for dest in waiting.get(stop, []):
            if len(bus) >= capacity:
                break
            if dest > stop:
                bus.append(dest)

    print(delivered)
main()
