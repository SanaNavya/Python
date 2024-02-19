a,b,c,d=map(float,input().split(","))
fa=a-a*c/100
fb=b-b*d/100
if fa<fb:
    print("first")   
elif fb<fa:
        print("second")
else:
    print("any")
