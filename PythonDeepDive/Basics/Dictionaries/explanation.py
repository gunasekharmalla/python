                                           Dictionary Basics
                          `````````````````````````````````````````````````````

What is a Dictionary in Python?
A dictionary is a collection of key-value pairs. 
It’s unordered, mutable, and indexed by keys (not by position like lists).

Syntax:

my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

Key Points:

Keys are unique
Values can be any data type
Defined using {} with key: value pairs

Examples
1. Creating a Dictionary

student = {
    "name": "Alice",
    "grade": "A",
    "marks": 95
}
print(student)

2. Accessing Values
print(student["name"])   # Output: Alice

3. Adding a New Pair
student["subject"] = "Math"
print(student)

4. Updating a Value
student["marks"] = 98

5. Deleting a Key-Value Pair
del student["grade"]

Useful Dictionary Methods
==========================================
Method	Description	Example
.get(key)	      Returns value or None if not found	student.get("name")
.keys()	        Returns all keys	student.keys()
.values()	      Returns all values	student.values()
.items()	      Returns all key-value pairs	student.items()
.update({...})	Updates dictionary with new pairs	student.update({"age": 20})
.pop(key)	      Removes and returns value	student.pop("name")
