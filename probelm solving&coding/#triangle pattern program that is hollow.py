#triangle pattern program that is hollow inside

for row in range(1,5):
    for col in range(1,8):
        if row==4 or row+col==5 or col-row==3:
             print("*",end="")
        else:
            print(end=" ")
    print()
#triangle pattern program that is hollow inside with user input
n=int(input("enter the number of rows"))
print()
for row in range(1,n+1):
    for col in range(1,2*n):
        if row==n or row+col==n+1 or col-row==n-1:
             print("*",end="")
        else:
            print(end=" ")
    print()
#type 3 triangle bottom pattern stars are even
n=int(input("enter the number of rows"))
k=2
print()
for row in range(1,n+1):
    for col in range(1,2*n):
        if row+col==n+1 or col-row==n-1:
             print("*",end="")
        elif row==n and col!=k:
             print("*",end="")
             k+=2
             
        
        else:
            print(end=" ")
    print()