n=int(input())
d={}
for i in range(n):
    k,v=map(str,input().split())
    d[k]=v
m=int(input("No of search items: ")) 
for i in range (m):
    s=input()
    if s in d:
        print(s,d[s])
    else:
        print("Not Found")
    
