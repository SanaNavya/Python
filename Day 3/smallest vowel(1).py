#write a python program to print smallest vowel repeating odd no.of times in the given string
s=input()
s1=""
count=0
for i in s:
    if i in "aeiouAEIOU":
        if s.count(i)%2!=0:
            s1+=i
            
print(min(s1))           
        
