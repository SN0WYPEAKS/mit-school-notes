########## Program to find and print the first 1000 prime numbers
# 1000th prime number is 7919
def printing_1000_prime_numbers():
    # Initialize variables to keep track of prime numbers and potential candidates
    # Count of prime numbers found
    primeAmount = 0
    # The number to be tested for primality
    potentialPrime = 2
    # Continue finding prime numbers until we have 1000 of them
    while primeAmount < 1000:
        # Start testing potentialPrime with 2, the smallest prime number
        primeTest = 2
        # Check if potentialPrime is divisible by any number from 2 to potentialPrime - 1
        while primeTest < potentialPrime:
            if potentialPrime % primeTest == 0:
                # If it's divisible, exit the loop
                break
            primeTest = primeTest + 1
        else:
            # If the inner loop completes without finding a divisor, potentialPrime is prime
            # Print the prime number found
            print(potentialPrime)
            # Increase the count of prime numbers
            primeAmount = primeAmount + 1
        # Move on to the next potential prime
        potentialPrime = potentialPrime + 1

printing_1000_prime_numbers()

########## Rough code that didn't quite work
# potentialPrime = 1
# primeTest = 1
# primeAmount = 0
# print(potentialPrime)
# while primeAmount < 1000:
#     while primeTest != potentialPrime:
#         if potentialPrime%primeTest == 0:
#             primeTest = primeTest + 1
#             break
#         else:
#             primeTest = primeTest + 1
#             if primeTest == potentialPrime:
#                 primeAmount = primeAmount + 1
