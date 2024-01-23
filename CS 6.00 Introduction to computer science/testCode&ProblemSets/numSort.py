########## Program to separate even and odd numbers from a user input
def numSort():
    even_numbers = []
    odd_numbers = []
    userInput = int(input("Enter a number that is more than 1 to find all odd and even numbers between it and 1: "))
    assert userInput > 1, 'The number must be greater than 1.'
    for i in range(1, userInput):
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    print("Heres all the even numbers:", even_numbers)
    print("Heres all the odd numbers:", odd_numbers)

def numSortSum():
    even_sum = 0
    odd_sum = 0
    userInput = int(input("Enter a number that is more than 1 to find and add all odd and even numbers together between it and 1: "))
    assert userInput > 1, 'The number must be greater than 1.'
    for i in range(1, userInput):
        if i % 2 == 0:
            even_sum = even_sum + i
        else:
            odd_sum = odd_sum + i
    print("Heres the sum of all even numbers:", even_sum)
    print("Heres the sum of all odd numbers:", odd_sum)
