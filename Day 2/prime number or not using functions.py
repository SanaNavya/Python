#write a python program to print prime numbers in a range using functions
def primenumber(n,m):
    for i in range(n,m+1):
        c=0
        for j in range(1,n+1):
            if i%j==0:
                c+=1
        if c==2:
            print(i)
n,m=int(input()),int(input())
primenumber(n,m)
    
