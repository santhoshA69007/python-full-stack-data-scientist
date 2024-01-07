#prime numbers
lower=int(input("enter the start:"))
upper=int(input("enter the end:"))
for num in range(lower,upper+1):
  if num>1:
    for i in range(2,num):
        if(num%i)==0:
        #   print("not a prime number",i)
            break
    else:
          print("prime number",num)