num = int(input("Enter the number: "))

i = 1
print(f"Factors of {num} are:")
while i <= num:
    if num % i == 0:
        print(i)
    i += 1
