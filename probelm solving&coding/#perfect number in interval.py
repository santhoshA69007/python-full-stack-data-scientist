#perfect number in interval
lower=int(input("enter the number  :"))
upper=int(input("enter the number  :"))
for num in range(lower,upper+1):
    result=0
    for i in range(1,num):
        if (num%i)==0:
            result+=i # so the i value is stored inside this adding up and comapred
    if num==result:
        print(f"{num} is a perfect number -/")
    # else:
    #     print(f"{num} is not a perfect number")