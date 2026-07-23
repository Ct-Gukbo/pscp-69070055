"""กระต่ายน้อยล้อมรั้วลวดหนาม"""
buy = input().split(" ")
price = int(input())
#3+3 5+5 * 4
long = int(buy[0])
width = int(buy[1])
floor = int(buy[2])
print(((long*2+width*2)*floor))
print(((long*2+width*2)*floor)*price)
