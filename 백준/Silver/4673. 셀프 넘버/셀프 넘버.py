d = set()

for num in range(10000):
    number = num
    num = str(num)
    for i in num:
        number += int(i)
    d.add(number)

for selfnum in range(1,10001):
    if selfnum not in d:
        print(selfnum)
