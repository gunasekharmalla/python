✅ Task 1: Count Vowels
✔️ Perfectly done!
You looped through the string and counted vowels correctly. Clean and simple.
s = "Hello World"
count = 0
for i in s:
    if i in 'AEIOUaeiou':
        count+=1
print(count)
==========================================================
✅ Task 2: Title Case
python
Copy
Edit
s1 = "python is fun"
print(s1.title())
========================================================
✅ Task 3: Replace Spaces with Hyphens
python
Copy
Edit
s2 = "python is awesome"
print(s2.replace(" ","-"))
============================================================
✅ Task 4: Palindrome Check
python
Copy
Edit
s3 = "madam"
print(s3 == s3[::-1])
===============================================================
import string

s4 = "Hello!!!, my name is..."
cleaned = ""
for i in s4:
    if i not in string.punctuation:
        cleaned += i
print(cleaned)
==================================================================
