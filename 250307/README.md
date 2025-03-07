# March 7, 2025
## Problem
### Closest Prime Numbers in Range

Given two positive integers left and right, find the two integers num1 and num2 such that:

    left <= num1 < num2 <= right
    Both num1 and num2 are prime numbers

    num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.

Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

## Initial impression
Prime numbers = Sieve of Eratoshtheses almost every time. For the second part, to minimize num2 - num1, I suppose we shall just compare adjacent primes and return the min difference. 

## Learning
My initial impression delivers a solution that is on the short side of the middle of the road, beating 59.38% of answers and being below several midfield spikes in the solution times graphs. A lot of people seem to just copy over the same code as someone else, what a strange use of a learning tool. 