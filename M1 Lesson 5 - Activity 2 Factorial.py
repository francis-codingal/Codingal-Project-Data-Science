def calculate_factorial(number):
    if number == 1:
        return number
    else:
        return number * calculate_factorial(number - 1)

val = int(input("Enter a number: "))

if val < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif val == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", val, "is", calculate_factorial(val))