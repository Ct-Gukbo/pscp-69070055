"""ผลคูณเลขโดดที่ไม่ใช่ศูนย์"""
number=input()
result=[]
for num in number:
    if int(num):
        result.append(num)
if not result:
    actual_result=0
else:
    actual_result=1
for uhh in result:
    actual_result*=int(uhh)
print(actual_result)
    