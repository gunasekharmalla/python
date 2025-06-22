def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(1234))  
Output: 10
-------------------------------------------------
def digit(n, sum_):
    if n == 0:
        return sum_
    sum_ += n % 10
    return digit(n // 10, sum_)
result = digit(1234, 0)
print(result)   
✅ Output: 10
------------------------------------------
