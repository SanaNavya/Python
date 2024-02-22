#write a python program to print sum of the matrix
r,c=int(input()),int(input())
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
print(l)
summ=0
for i in l:
    summ+=sum(i)
print(summ)    

