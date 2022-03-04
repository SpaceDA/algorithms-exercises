"""EXERCISE 1.1.20"""

# Write a recursive static method that computes the value of ln (n!)
import math


def get_ln(n):
    # ln(1) = 0
    if n == 1:
        return 0
    else:
        # ln(m*n) = ln(n) + ln(m)
        return math.log(n) + get_ln(n-1)




