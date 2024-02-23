#write a python program to display n prime and composite numbers
def isprime(m):
    for i in range(2,m):
        if m%1==0:
            return"composite"
    else:
            return "prime"
n=int(input())
d={}
for i in range(n):
    k=i+1
    v=isprime(i)
    d[k]=v
print(d)    
