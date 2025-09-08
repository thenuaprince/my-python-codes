n = int(input("Enter : "))
x=1
for i in range(1,n):
    for j in range(i):
        print(x,end=" ")
        x=x+1
    print()