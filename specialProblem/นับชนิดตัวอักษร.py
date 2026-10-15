"""นับชนิดตัวอักษร"""
s=input().replace(" ",'')
upper=0
lower=0
number=0
for char in s:
    if char.isupper():
        upper+=1
    elif char.islower():
        lower+=1
    elif char.isnumeric():
        number+=1
print(upper,lower,number)
