"""Frame"""
def main():
    """Frame"""
    WORD = str(input())
    FRAME = len(WORD) + 2
    for _ in range(FRAME) :
        print("*" ,end="")
    print("")
    print("*"+(WORD)+"*")
    for _ in range(FRAME) :
        print("*" ,end="")
main()
