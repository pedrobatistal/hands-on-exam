#2. Write a program to check if a string is palindrome. A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam, nurses run.(1 point)

def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_string = ''.join(s.split()).lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Example: Check if a string is a palindrome
input_string = input("Type a string to check if it's a palindrome: ")
result = is_palindrome(input_string)

if result:
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")
