"""Elo"""
RA = int(input())
RB = int(input())
PLAYER = str(input())
EA = 1 / (1+(10**((RB-RA)/400)))
EB = 1 / (1+(10**((RA-RB)/400)))
if PLAYER == "A" :
    print(f"{EA:.2f}")
elif PLAYER == "B" :
    print(f"{EB:.2f}")
