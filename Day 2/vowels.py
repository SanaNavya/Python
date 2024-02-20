#write a python program to print the count of vowels in even and odd position
s=input()
e,o=0,0
for i in range (len(s)):
    if i%2==0:
        if s[i] in"aeiouAEIOU":
            e+=1
        else:
            if s[i] in"aeiouAEIOU":
                 o+=1
print(e,o)                 
        
