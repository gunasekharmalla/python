Python Built-in Functions
Python provides several built-in functions that eliminate the need for explicit loops, making code more efficient and readable. Below are some commonly used built-in functions with explanations and syntax.

1.Summing Elements: sum()
The sum() function calculates the total sum of all elements in an iterable.

Syntax:
sum(iterable, start)
iterable: A sequence of numbers (list, tuple, etc.).
start (optional): A value added to the sum (default is 0).

2.Finding Maximum and Minimum: max() and min()
max(): Returns the largest element in an iterable.
min(): Returns the smallest element in an iterable.

Syntax:
max(iterable, key=None)  
min(iterable, key=None)
iterable: A sequence (list, tuple, or string).
key (optional): A function to customize sorting criteria.

3.Sorting Elements: sorted()
The sorted() function returns a new sorted list from an iterable.

Syntax:
sorted(iterable, key=None, reverse=False)
key (optional): A function to determine sorting criteria.
reverse (optional): If True, sorts in descending order.

4.Filtering Elements: filter()
The filter() function extracts elements from an iterable based on a condition.

Syntax:
filter(function, iterable)
function: A function that returns True or False.
iterable: The sequence to filter.

5.Applying Functions: map()
The map() function applies a function to each element of an iterable.

Syntax:
map(function, iterable)
function: A function applied to each element.
iterable: The sequence to transform.

6.Reducing Elements: reduce()
The reduce() function from functools applies a function cumulatively to elements in an iterable.

Syntax:
from functools import reduce
reduce(function, iterable, initializer=None)

function: A function that takes two arguments.
iterable: A sequence of elements.
initializer (optional): A starting value.

7.Checking Membership: any() and all()
any(): Returns True if at least one element in the iterable is True.
all(): Returns True if all elements in the iterable are True.

Syntax:
any(iterable)
all(iterable)
iterable: A sequence of truthy or falsy values.

## This is the brief Summary of built in functions
 
Function			Purpose
sum()			-->	Computes the sum of elements in an iterable
max() / min()		-->	Finds the maximum/minimum value
sorted()		-->	Returns a sorted list
filter()		-->	Extracts elements that satisfy a condition
map()			-->	Applies a function to each element in an iterable
reduce()		-->	Reduces an iterable to a single value using 