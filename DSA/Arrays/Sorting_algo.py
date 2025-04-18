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

