n = int(input("Enter a number of stars: "))

for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()

for i in range(n,1,-1):
    for j in range(1,i):
        print("*",end="")
    print()