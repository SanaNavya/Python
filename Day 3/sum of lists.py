#write a python program to print sum of odd numbers in the range
n,m=int(input()),int(input())
l=[i for i in range(n,m+1)if i%2!=0]
print(sum(l))
