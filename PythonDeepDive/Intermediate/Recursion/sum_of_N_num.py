def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(4))

call stack trace:

sum_n(4)
→ 4 + sum_n(3)

sum_n(3)
→ 3 + sum_n(2)

sum_n(2)
→ 2 + sum_n(1)

sum_n(1)
→ 1 + sum_n(0)

sum_n(0)
→ returns 0

output:
10

sum_n(4)
  └─ sum_n(3)
       └─ sum_n(2)
            └─ sum_n(1)
                 └─ sum_n(0) = 0
            ←─ 1 + 0 = 1
       ←─ 2 + 1 = 3
  ←─ 3 + 3 = 6
←─ 4 + 6 = 10

