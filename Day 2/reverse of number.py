#write a python program to print reverse of a number
n=int(input())
rev=0
while n>0:
    num=n%10
    rev=rev*10+num
    n//=10
print(rev)
