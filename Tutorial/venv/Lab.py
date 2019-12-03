def sum_recursion(number):
    if (number==1):
        return 1
    return number + sum_recursion(number-1)

print(sum_recursion(10))