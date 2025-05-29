✅ Problem: Sort Characters By Frequency


🧠 Problem Statement

Given a string s, sort it in descending order based on character frequency.
Return the sorted string.


---

🎯 Example

Input:  s = "tree"
Output: "eert"  # or "eetr" (as 'e' occurs twice, others once)

Input:  s = "cccaaa"
Output: "aaaccc" or "cccaaa"


---

✅ Approach: Frequency Dictionary + Sorting

🔧 Step-by-step Logic:

1. Count the frequency of each character.


2. Sort characters by frequency in descending order.


3. Build the result by repeating each character by its frequency.




---

🧑‍💻 Code:

def frequencySort(s: str) -> str:
    freq = {}

    # Step 1: Count frequencies
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Step 2: Sort characters by freq (high to low)
    sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Step 3: Build result string
    result = ""
    for char, count in sorted_chars:
        result += char * count

    return result


---

🔍 Dry Run

Input: "tree"

freq → { 't': 1, 'r': 1, 'e': 2 }

sorted_chars → [('e', 2), ('t', 1), ('r', 1)]

result → "ee" + "t" + "r" → "eetr"


✅ Final Output: "eetr" (or "eert" — both valid)


---

⏱️ Time Complexity:

Counting → O(n)

Sorting → O(k log k), where k = number of unique chars (≤ 26 for lowercase)

Result Construction → O(n)
=========================
tip: using counter 
from collections import Counter

def frequencySort(s: str) -> str:
    count = Counter(s)
    return ''.join(char * freq for char, freq in count.most_common())
