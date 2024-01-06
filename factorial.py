import math
#factorial program
#using built in function
n=int(input("enter a number"))
n=math.factorial(n)
print(n)

#using recurion function
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
num1=int(input("enter a number"))
print(fact(num1))


#using loop with step 
num2=int(input("enter a number"))
sum=1

for i in range(num2,1,-1):
    sum=sum*i
    
print(sum)