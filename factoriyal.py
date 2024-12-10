# Function to calculate the factorial
def factorial(n):
    # If n is 0 or 1, return 1 (base case)
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Input from the user
num = int(input("Enter a number: "))

# Check if the number is negative
if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    # Calculate the factorial
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
