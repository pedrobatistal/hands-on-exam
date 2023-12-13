#1. Write a program that prints the Fibonacci series up to a given number, e.g., 1 1 2 3 5 8 13 ... (1 point)

def fibonacci(n):
    if n < 0:
        return "Please enter a non-negative integer."

    fib_series = [1, 1]
    
    while fib_series[-1] + fib_series[-2] <= n:
        fib_series.append(fib_series[-1] + fib_series[-2])

    return fib_series

# Example: Print Fibonacci series up to a given number
given_number = int(input("Type a non-negative integer to calculate its Fibonacci series: "))
result = fibonacci(given_number)
print(result)