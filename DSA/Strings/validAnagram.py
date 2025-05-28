 valid anagram

Given two strings s and t, return True if t is an anagram of s, and False otherwise.

 Example

Input: s = "anagram", t = "nagaram"
Output: True

Input: s = "rat", t = "car"
Output: False
------------
✅ Approach 1: Sorting

Two anagrams will have the same characters in the same frequency, so after sorting both strings, they should be equal.

🔧 Code:

def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
⏱️ Time Complexity:
Sorting → O(n log n)
--------------------
✅ Approach 2: Using Dictionary / Counter
Compare the frequency of each character in both strings.

🔧 Code:

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    for ch in s:
        count_s[ch] = count_s.get(ch, 0) + 1

    for ch in t:
        count_t[ch] = count_t.get(ch, 0) + 1

    return count_s == count_t
🔍 Dry Run
Input: "anagram" and "nagaram"

count_s: {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}

count_t: {'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}

✅ count_s == count_t → return True
------------------------------------
apporoach 3:
✅ Bonus: Use collections.Counter
You can simplify it with Python's Counter:


from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
