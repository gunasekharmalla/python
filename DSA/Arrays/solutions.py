Problem 1: 
    Find the Largest and Smallest Element in an Array
    Problem Statement:
    Given an array of integers, find the smallest and largest elements.
    Example:
    Input: [3, 5, 1, 2, 4, 8]
    Output: Smallest: 1, Largest: 8
    #program:
    maxi, mini = float('-inf'),float('inf')
    for i in nums:
        if i > maxi:
            maxi = i
        if i < mini:
            mini = i 
    print(maxi,mini)
