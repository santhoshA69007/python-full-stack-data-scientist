#Python Pattern Programs - Printing Strings in Right Triangle Shape
n=input("enter a text to form right triangle       :")

for row in range(len(n)):
    for col in range(0,row+1):
        
         print(n[col],end=" ")
         

     
    print()