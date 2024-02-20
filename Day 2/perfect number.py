#write apython program to check whether given number is perfect number or not
n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("perfect number")
else:
    print("not a perfect number")
