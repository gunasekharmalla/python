                                            🔎 Topic: Sorting Algorithms
                                          ===================================

Basic Sorting Algorithms:
    Bubble Sort
    Selection Sort
    Insertion Sort

Efficient Sorting Algorithms:
    Merge Sort
    Quick Sort
                      Bubble sort 
                  =====================

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, 
compares adjacent elements, and swaps them if they are in the wrong order.

🔎 How it Works:
      Start from the first element.
      Compare it with the next element.
      If the first element is greater than the second, swap them.
      Continue this for all elements in the array.
      After each pass, the largest element moves to its correct position.
      Repeat until no more swaps are needed.

📘 Example:
Input:
5 1 4 2 8

Pass 1:
1 5 4 2 8  → Swap (5,1)
1 4 5 2 8  → Swap (5,4)
1 4 2 5 8  → Swap (5,2)
1 4 2 5 8  → No Swap (5,8)

Pass 2:
1 4 2 5 8  → No Swap (1,4)
1 2 4 5 8  → Swap (4,2)
1 2 4 5 8  → No Swap (4,5)
1 2 4 5 8  → No Swap (5,8)
....... pass n-1


Program:

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swap happens
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swap, break
        if not swapped:
            break

arr = list(map(int, input("Enter numbers separated by space: ").split()))
bubble_sort(arr)
print("Sorted Array:", arr)

Sorted Array: 1 2 4 5 8


              Merge Sort
        ========================

Program:

def Merge_sorting(arr):
    if not arr:
        return None
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        Merge_sorting(left_arr)
        Merge_sorting(right_arr)
        
        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k] = right_arr[j]
                j+=1
            k+=1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i, k = i+1, k+1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j, k = j+1, k+1
    return arr
lst = [3, 6, 1, 8, 2, 5, 9]
lst = Merge_sorting(lst)
print(f"sorted list : {lst}")

sorted list: [1, 2, 3, 5, 6, 8, 9]
===========================
# insertion sort 
arr = [12, 11,  13,  5,  6]
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  # Current element to be inserted
        j = i - 1
        # Shift elements to the right to create space for key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = list(map(int, input("Enter numbers separated by space: ").split()))
insertion_sort(arr)
print("Sorted Array:", arr)

Output : 
Sorted Array: [5, 6, 11, 12, 13]
