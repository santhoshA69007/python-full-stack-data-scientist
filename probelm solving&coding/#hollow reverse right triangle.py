#hollow reverse right triangle
n=int(input("enter the no of rows to be printed:"))
for row in range(n):
    for col in range(n):
        if  row==0 or col==(n-1) or row==col :
            print("*",end="")
        else:
            print(end=" ")
    print()
