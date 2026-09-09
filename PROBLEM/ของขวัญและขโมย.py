"""ของขวัญและขโมย"""
def main():
    """ของขวัญและขโมย"""
line = input().split()
N = int(line[0])
K = int(line[1])
T = int(line[2])
current = 1
count = 1
if current == T:
    print(count)
else:
    while True:
        current = current + K
        while current > N:
            current = current - N
        if current == 1:
            break
        count = count + 1
        if current == T:
            break
    print(count)
main()
