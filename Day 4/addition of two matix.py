#write a python program to make addition of two matrix
r,c=int(input()),int(input())
l1,l2,l3=[],[],[0]*r
for i in range(r):
    l3[i]=[0]*c
for i in range(r):
    l1.append(tuple(map(int,input().split())))
for i in range(r):
    l2.append(tuple(map(int,input().split())))
for i in range (r):
    for j in range(c):
        l3[i][j]=l1[i][j]+l2[i][j]
for i in l3:
    print(i)
