# Importing the math module
import math

def is_prime(num):
    # Check if the number is less than 2 (not prime)
    if num < 2:
        return False

    # Loop through numbers from 2 to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False  # Number is not prime

    return True  # Number is prime

# Example usage
test_number = 29  # You can change this number to test others
result = is_prime(test_number)

# Print the result
print(f"The number {test_number} is prime: {result}")

