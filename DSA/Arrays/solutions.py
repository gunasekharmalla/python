Problem 1: 
    Find the Largest and Smallest Element in an Array
    Problem Statement:
    Given an array of integers, find the smallest and largest elements.
    #program:
    maxi, mini = float('-inf'),float('inf')
    for i in nums:
        if i > maxi:
            maxi = i
        if i < mini:
            mini = i 
    print(maxi,mini)

 Example:
    Input: [3, 5, 1, 2, 4, 8]
    Output: Smallest: 1, Largest: 8
=================================================================================
Problem 2: Second Largest and Second Smallest Element
#Program:

    arr =[12,35,1,10,34,1]
    arr.sort()
    large =arr[-1]
    small = arr[0]
    for right in range(len(arr)-2,-1,-1):
        if arr[right] == large:
            continue 
        else:
            print("smax=",arr[right])
            break
    
    for right in range(1,len(arr)):
        if arr[right] == small:
            continue
        else:
            print("ssmall=",arr[right])
            break
            
Input: [12, 35, 1, 10, 34, 1]
Output: Second Largest: 34, Second Smallest: 10
=================================================================
problem 3: Check if an Array is Sorted
arr = [1, 2, 3, 4, 5, 1]
b = True

for i in range(1, len(arr)):
    if arr[i] < arr[i - 1]:
        b = False
        break
        
print(b)

Input: [1, 2, 3, 4, 5]
Output: True

Input: [1, 3, 2, 4, 5]
Output: False
====================================================================
