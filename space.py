n = 5
for i in range(n, 0, -1):      
    for j in range(1, i + 3):  
        if j == 1 or j == i + 2:
            print("*", end=" ")
        else:
            print("_", end=" ")
    print()
