#  Basic examples of Built in Functions examples.py
1. sum()
2. max() min()
3. sorted()
4. filter()
5. map()
6. reduce()
7. membership any() all()

# 1. Summing Elements: 
1. sum() 
numbers = [10, 20, 30, 40]
print(sum(numbers))  # Output: 100
print(sum(numbers, 50))  # Output: 150

# 2. Finding Maximum and Minimum: 
2. max() and min()
values = [5, 10, 2, 8, 15]
print(max(values))  # Output: 15
print(min(values))  # Output: 2

words = ["apple", "banana", "cherry"]
print(max(words, key=len))  # Output: "banana"
print(min(words, key=len))  # Output: "apple"

# 3. Sorting: 
3. sorted()
numbers = [3, 1, 4, 1, 5, 9]
print(sorted(numbers))  # Output: [1, 1, 3, 4, 5, 9]
print(sorted(numbers, reverse=True))  # Output: [9, 5, 4, 3, 1, 1]
print(sorted(words, key=len))  # Output: ['apple', 'cherry', 'banana']

# 4. Filtering Elements: 
4. filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

short_words = list(filter(lambda w: len(w) <= 5, words))
print(short_words)  # Output: ['apple']

# 5. Applying Functions: 
5. map()
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # Output: [1, 4, 9, 16, 25]

uppercase_words = list(map(str.upper, words))
print(uppercase_words)  # Output: ['HELLO', 'WORLD']

# 6. Reducing: 
6. reduce()
from functools import reduce

product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

sum_with_initial = reduce(lambda x, y: x + y, numbers, 10)
print(sum_with_initial)  # Output: 25

# 7. Checking Membership: 
7. any() and all()
values = [0, 1, 2, 3]
print(any(values))  # Output: True
print(all(values))  # Output: False

words = ["apple", "", "banana"]
print(any(words))  # Output: True
print(all(words))  # Output: False

## These are the basic examples of Built In Functions in python 
