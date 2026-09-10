"""ไพ่ 44 ใบ"""
def main():
    """ไพ่ 44 ใบ"""
    cardpoint = {"2": "2", "3": "3", "4": "4", "5": "5",
                 "6": "6", "7": "7", "8": "8", "9": "9", "10": "10"}
    cardpointplus = ["J", "Q", "K", "A"]
    cardface = ["D", "H", "S", "C"]

    code = input().strip().upper()

    rank_code = code[:-1]
    suit_code = code[-1]

    rank_word = ""
    suit_word = ""

    if rank_code in cardpoint:
        rank_word = cardpoint[rank_code]
    elif rank_code in cardpointplus:
        if rank_code == "A":
            rank_word = "ace"
        elif rank_code == "J":
            rank_word = "jack"
        elif rank_code == "Q":
            rank_word = "queen"
        elif rank_code == "K":
            rank_word = "king"

    if suit_code in cardface:
        if suit_code == "D":
            suit_word = "diamonds"
        elif suit_code == "H":
            suit_word = "hearts"
        elif suit_code == "S":
            suit_word = "spades"
        elif suit_code == "C":
            suit_word = "clubs"
    print(f"{rank_word} of {suit_word}")
main()
