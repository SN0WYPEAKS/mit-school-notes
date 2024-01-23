########## More concise code
import math

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        return True

# Function to calculate the sum of logarithms of prime numbers up to 'n'
def sum_of_prime_logs(n):
    # Iterate through numbers from 2 to 'n' and checks if the number is prime using the is_prime function
    prime_logs_sum = sum(math.log(i) for i in range(2, n + 1) if is_prime(i))
    return prime_logs_sum

# Prompt the user to enter a value for 'n'
n = int(input("Enter a value for 'n': "))

# Check if 'n' is less than 2 and provides a message if the input is invalid
if n < 2:
    print("Please enter a value of 'n' greater than or equal to 2.")
else:
    # Calculate the sum of prime logs and display results
    prime_logs_sum = sum_of_prime_logs(n)
    print(f"Sum of logarithms of primes from 2 to {n}: {prime_logs_sum}")
    print(f"Value of 'n': {n}")
    # Calculate and display the ratio of sum of logs to 'n'
    ratio = prime_logs_sum / n
    print(f"Ratio of sum of logs to 'n': {ratio}")

########## Original code
# import math

# def is_prime(num):
#     if num <= 1:
#         return False
#     if num == 2:
#         return True
#     if num % 2 == 0:
#         return False
#     for i in range(3, int(math.sqrt(num)) + 1, 2):
#         if num % i == 0:
#             return False
#     return True

# def sum_of_prime_logs(n):
#     prime_logs_sum = 0
#     for i in range(2, n + 1):
#         if is_prime(i):
#             prime_logs_sum += math.log(i)
#     return prime_logs_sum

# # Input: Get the value of 'n' from the user
# n = int(input("Enter a value for 'n': "))

# if n < 2:
#     print("Please enter a value of 'n' greater than or equal to 2.")
# else:
#     prime_logs_sum = sum_of_prime_logs(n)
#     print(f"Sum of logarithms of primes from 2 to {n}: {prime_logs_sum}")
#     print(f"Value of 'n': {n}")
#     ratio = prime_logs_sum / n
#     print(f"Ratio of sum of logs to 'n': {ratio}")
