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

Problem 2: Second Largest and Second Smallest Element
Input: [12, 35, 1, 10, 34, 1]
Output: Second Largest: 34, Second Smallest: 10
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
        

