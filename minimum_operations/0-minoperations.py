#!/usr/bin/python3

"""
    In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
    Copy All and Paste. Given a number n, write a method that calculates
    the fewest number of operations needed to result
    in exactly n H characters in the file.
"""

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

