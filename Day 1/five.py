a,b=map(float,input().split(","))
output=a/5
if output%5==0:
    print("multiple of 5")
result=(a-b)
if result%5==0:
    print(result)
else:
    print("not a multiple")
    
