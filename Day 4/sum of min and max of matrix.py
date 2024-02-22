#write a python program to print sum of maximum and minimum element in a matrix using tuple
r,c=int(input()),int(input())
l=[]
for i in range(r):
    l.append(tuple(map(int,input().split())))
min,max=1000,0
for i in l:
    print(i)
    for j in i:
        if j>max:
            max=j
        if j<min:
            min=j
print(max+min)            
