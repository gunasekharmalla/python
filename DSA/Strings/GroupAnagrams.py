def groupAnagrams(strs):
    anagrams = {}

    for word in strs:
        key = ''.join(sorted(word))  # sorted characters form the key

        if key not in anagrams:
            anagrams[key] = []  # create new list for this key

        anagrams[key].append(word)  #if yes add the word to the group
    return list(anagrams.values())

Dry Run

Input: 
["eat", "tea", "tan", "ate", "nat", "bat"]

"eat" → "aet" not in dict → create {"aet": ["eat"]}

"tea" → "aet" exists → append → {"aet": ["eat", "tea"]}

"tan" → "ant" not in dict → {"ant": ["tan"]}

"ate" → "aet" exists → append → {"aet": ["eat", "tea", "ate"]}

"nat" → "ant" exists → {"ant": ["tan", "nat"]}

"bat" → "abt" not in dict → {"abt": ["bat"]}


Final Output:

[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


