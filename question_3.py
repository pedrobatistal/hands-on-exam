#3. Write a program to check if a number is prime. Prime numbers are whole numbers greater than 1, that have only two factors, 1 and the number itself, e.g., 3, 5, 7, 11, 13, 17, and etc. (1 point)
def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # Number is divisible by a factor other than 1 and itself
    
    return True  # Number is prime

# Example: Check if a number is prime
input_number = int(input("Type an integer to check if it's a prime number: "))
result = is_prime(input_number)

if result:
    print(f"{input_number} is a prime number.")
else:
    print(f"{input_number} is not a prime number.")
