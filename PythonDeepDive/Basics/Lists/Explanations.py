                                   1: Introduction to Lists
                      ================================================
What is a List?
A list is a built-in data type in Python that can store multiple items in a single variable. 
Lists are ordered, changeable (mutable), and allow duplicate values.

Syntax:
my_list = [1, 2, 3, 4, 5]

It can hold any type:
mixed_list = [1, "hello", 3.14, True]

                    PART 2: Basic Operations on Lists
        ==============================================================
1. Creating a List
fruits = ["apple", "banana", "cherry"]

2. Accessing Elements (Indexing)
print(fruits[0])   # Output: apple
print(fruits[-1])  # Output: cherry (last item)

3. Slicing a List
print(fruits[0:2])   # Output: ['apple', 'banana']

4. Changing Values
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

5. List Length
print(len(fruits))  # Output: 3

                      PART 3: List Methods (Beginner Level)
              =======================================================
Method	Description
        append()	Adds element at the end
        insert()	Adds element at a specific position
        remove()	Removes specific value
        pop()	    Removes item at index (default last)
        clear()	  Removes all items
        index()	  Finds the index of an element
        count()	  Counts how many times a value appears

Examples:
nums = [1, 2, 3]
nums.append(4)        # [1, 2, 3, 4]
nums.insert(1, 10)    # [1, 10, 2, 3, 4]
nums.remove(2)        # [1, 10, 3, 4]
print(nums.pop())     # Removes 4
nums.clear()          # []

TASKS for Beginner Level
============================
Create a list of your 5 favorite movies.
Replace the 2nd movie with a new one.
Add one more movie at the end.
Remove the 4th movie.
Print the list and its length.
