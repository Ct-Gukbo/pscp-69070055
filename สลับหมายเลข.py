"""สลับหมายเลข"""
Number = input()
Operator = input()
Reverse = Number[-1]+Number[0]
if 10 <= int(Number) <= 99:
    if Operator == "+" :
        print (int(Number) , str(Operator) , int(Reverse) ,"=", int(Number) + int(Reverse))
    elif Operator == "*" :
        print (int(Number) , str(Operator) , int(Reverse) ,"=", int(Number) * int(Reverse))
else :
    print()
