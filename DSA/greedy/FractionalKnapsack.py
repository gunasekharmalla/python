                                ⚒️ Greedy Problem : Fractional Knapsack
💡 Problem Statement:
You are given:
n items
Each item has:
a value
a weight
A knapsack can carry at most W weight.
⏱️ You can take fractions of items.
🎯 Goal:
Maximize the total value that fits in the knapsack.
  
📥 Example:
items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
capacity = 50
✅ Output:
      240.0

Because:
Take all of item 2 → value = 100
Take all of item 3 → value = 120
Remaining capacity = 50 - 20 - 30 = 0
Total = 220 + 20 (partial of item 1) = 240

🧠 Greedy Strategy:
Sort items by value/weight ratio (descending)
Start picking items until full
If item doesn’t fit fully, take fraction
===================================================================
✅ Python Code:
def fractional_knapsack(items, capacity):
    # Sort by value-to-weight ratio
    items.sort(key=lambda x: x[0]/x[1], reverse=True)

    total_value = 0.0

    for value, weight in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            fraction = capacity / weight
            total_value += value * fraction
            break

    return total_value
============================================================================

items = [(60, 10), (100, 20), (120, 30)]
capacity = 50

print("Max value in knapsack:", fractional_knapsack(items, capacity))
✅ Output:
Max value in knapsack: 240.0
Expected: You should pick 1 full item + part of another
