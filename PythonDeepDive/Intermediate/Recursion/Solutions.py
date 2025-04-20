        1. Factorial of a Number

def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive call

print(factorial(5))  # Output: 120
===============================================

        2. Fibonacci Series (Recursive)

def fibonacci(n):
    if n == 0 or n == 1:  # Base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive call

print(fibonacci(6))  # Output: 8

====================================================
        3. Sum of First N Natural Numbers

def sum_n(n):
    if n == 0:  # Base case
        return 0
    return n + sum_n(n - 1)  # Recursive call

print(sum_n(5))  # Output: 15
========================================================
          4. Reverse a String Using Recursion

def reverse_string(s):
    if len(s) == 0:  # Base case
        return s
    return reverse_string(s[1:]) + s[0]  # Recursive call

print(reverse_string("hello"))  # Output: "olleh"
===========================================================
          5. Checking if a Number is Palindrome

def is_palindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return is_palindrome(s, left + 1, right - 1)  # Recursive call

s = "madam"
print(is_palindrome(s, 0, len(s) - 1))  # Output: True
==============================================================
