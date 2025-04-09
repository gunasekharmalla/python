
name = "Alice"
greeting = 'Hello'
multiline = """This is 
a multiline string"""

print(name[0])        # A
print(name[-1])       # e
===============================
## Common Operations ##

# Concatenation
print("Hello " + name)

# Repetition
print("Hi! " * 3)

# Membership
print("A" in name)     # True

# Slicing
print(name[1:4])       # lic
======================================
## Built In String Methods ##

s = "  python programming  "

print(s.upper())       # '  PYTHON PROGRAMMING  '
print(s.lower())       # '  python programming  '
print(s.strip())       # 'python programming'
print(s.replace("python", "java"))   # '  java programming  '
print(s.split())       # ['python', 'programming']
print(s.find("prog"))  # 9
print(s.count("m"))    # 2
=========================================
## Advanced String Usage ##

# f-strings
name = "Alice"
age = 21
print(f"My name is {name} and I'm {age} years old.")

# Join iterable to string
words = ["Python", "is", "fun"]
print(" ".join(words))  # Python is fun
================================================
## example ##

email = "contact@company.com"
if email.endswith(".com") and "@" in email:
    print("Valid email")
==================================================
