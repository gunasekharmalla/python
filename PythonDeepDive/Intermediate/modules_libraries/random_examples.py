import random

nums = [10, 20, 30, 40, 50]
print("Random int:", random.randint(1, 100))
print("Random choice from list:", random.choice(nums))
print("Shuffled list:", random.sample(nums, len(nums)))

Output:
        Random int: 71
        Random choice from list: 10
        Shuffled list: [50, 20, 30, 40, 10]
-------------------------------------------------------------------------------------
