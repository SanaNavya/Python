n=int(input("enter no of students: "))
m=int(input("enter no of subjects: "))
d={}
for i in range(n):
    k=input("enter roll no: ")
    v={}
    for j in range(m):
        sub=input("enter the subject name: ")
        marks=int(input("enter marks: "))
        v[sub]=marks
    d[k]=v
for i in d:
    l=list(d[i].values())
    print(f"{i}: {sum(l)/m}")
