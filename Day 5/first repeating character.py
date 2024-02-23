#find fist representing character
s=input()
for i in s:
    if s.count(i)>1:
        print(i)
        break
else:
    print('.')
