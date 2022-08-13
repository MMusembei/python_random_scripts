'''write a .py program to compute the sum of
    the terms of series: 1+2+4+16+32+64+..+n,
    where n is an input '''

n = int(input("Enter n: "))
total = 0
for j, i in enumerate(range(4, n + 4, 4)):
    if j % 2 == 1:
        i = -i
    total += i
print()
print("The sum is: %s"%(total))
