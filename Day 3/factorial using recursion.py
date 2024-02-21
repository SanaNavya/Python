#write a python program to print the factorial of given number
def fact(n):
    if n<1:
        return 1
    else:
        return n*fact(n-1)
n=int(input())
print(fact(n))
