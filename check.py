number = int(input("Enter a number: "))

divisible_by_3 = number % 3 == 0

last_digit = abs(number) % 10
is_last_digit_4 = last_digit == 4

if divisible_by_3 and is_last_digit_4:
    print("The number is divisible by 3 and the last digit is 4.")
else:
    print("The number does not satisfy both conditions.")
