num = int(input("Enter a number: "))

digits = str(num)
num_digits = len(digits)

total_sum = sum(int(digit) ** num_digits for digit in digits)

if total_sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")