🧩 Problem 9: Roman to Integer

> LeetCode #13 — Decode a Roman numeral into its integer value.


---

📝 Problem Statement:

Given a string s containing a Roman numeral, convert it to an integer.

---

🏛️ Roman Numerals and Their Values:

Symbol	Value

I	1
V	5
X	10
L	50
C	100
D	500
M	1000


Special subtractive cases:

IV = 4, IX = 9

XL = 40, XC = 90

CD = 400, CM = 900



---

🔧 Example:

Input: "III"
Output: 3

Input: "IV"
Output: 4

Input: "MCMXCIV"
Output: 1994
Explanation:
M (1000) + CM (900) + XC (90) + IV (4)


---

✅ Core Idea:

Go from left to right:

If current value < next value → subtract

Else → add



---

✅ Code:

def romanToInt(s: str) -> int:
    roman = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev = 0

    for ch in reversed(s):
        curr = roman[ch]
        if curr < prev:
            total -= curr
        else:
            total += curr
        prev = curr

    return total


---

🔍 Dry Run: "MCMXCIV"

Reverse → "V", "I", "C", "X", "M", "C", "M"

Char	Value	Action	Total

V	5	+5	5
I	1	-1	4
C	100	+100	104
X	10	-10	94
M	1000	+1000	1094
C	100	-100	994
M	1000	+1000	1994

---
⏱ Time Complexity:
O(n) where n = len(s)


