#write a python program to print whether given element is enagram or not
n,m=map(str,input().split())
if len(n) == len(m):
    if sorted(list(n)) == sorted(list(m)):
        print(sorted(list(n)))
        print(sorted(list(m)))
        print(True)
    else:
        print(False)
else:
    print(False)
