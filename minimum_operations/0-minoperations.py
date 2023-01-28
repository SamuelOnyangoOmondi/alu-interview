#!/usr/bin/python3
def min_operations(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    i = 2
    operations = 0
    while i <= n:
        while n % i == 0:
            operations += i
            n = n // i
        i += 1
    return operations

