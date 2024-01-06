#pattern program -1
n=int(input("enter the number of rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
#pattern program -1 same name in each row
n=int(input("enter the number of rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()