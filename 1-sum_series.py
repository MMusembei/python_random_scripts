n = int(input("Enter n: "))
prev_num = 1
sum = 0
while(prev_num<=n):
    sum =sum+prev_num
    prev_num = prev_num*2

print("The sum is: %s"%(sum))
