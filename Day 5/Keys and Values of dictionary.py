#write a python program to take dictionary as input and print keys and values of the dictionary which is taken at runtime.
n=int(input("Enter no of items:"))
d={}
for i in range (n):
    key= input("Key: ")
    value=input("Value: ")
    d[key]=value
print(d)    
