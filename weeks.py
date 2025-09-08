n = int(input("Enter a number (1-7): "))
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
if 1 <= n <= 7:
    print(days[n-1])
else:
    print("Invalid input")
