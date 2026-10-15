"""ตรวจสอบรหัสผ่าน"""
password=input()
Valid=False
upper=False
lower=False
number=False
if len(password) < 8:
    Valid=False
else:
    for char in password:
        if char.isupper():
            upper=True
        elif char.islower():
            lower=True
        elif char.isdigit():
            number=True
if upper and lower and number:
    Valid=True
if Valid:
    print('VALID')
else:
    print('INVALID')
