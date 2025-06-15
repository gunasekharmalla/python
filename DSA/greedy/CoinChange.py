                  🚀 Greedy Problem : Coin Change (Minimum Coins)
💡 Problem:

Given coin denominations and a target amount, find the minimum number of coins needed to make that amount.
Assumption: You can take unlimited coins of each type.

📥 Input:
coins = [1, 2, 5, 10]
amount = 27
🎯 Output:
4 (10 + 10 + 5 + 2)

🧠 Greedy Strategy:

Sort coins in descending order
Always pick the biggest coin ≤ remaining amount
Repeat until total is made.
===================================================================================
def min_coins(coins, amount):
    coins.sort(reverse=True)  # Step 1: Sort in descending order
    count = 0
    result = []

    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
            count += 1

    if amount != 0:
        return -1  # Not possible to make exact change
    return count, result
=======================================================================================
# Test
coins = [1, 2, 5, 10]
amount = 27

count, used = min_coins(coins, amount)
print("Minimum coins used:", count)
print("Coins used:", used)
✅ Output:

Minimum coins used: 4
Coins used: [10, 10, 5, 2]

⚠️ Warning: Greedy doesn't always work for coin change

For example:
coins = [1, 3, 4]
amount = 6

Greedy gives: 4+1+1 = 3 coins
Optimal is: 3+3 = 2 coins

So when coin denominations are weird → use Dynamic Programming instead.

🔥 Task:
Try this with coins = [1, 5, 6, 9] and amount = 11.
See what greedy gives, and check if it’s optimal.

✅ Answer:
coins = [1, 5, 6, 9]
amount = 11
Greedy gives: [9, 1, 1] → 3 coins
Optimal is: [6, 5] → only 2 coins
