# Feb 27, 2025
## Problem
### Length of Longest Fibonacci Subsequence

A sequence x1, x2, ..., xn is Fibonacci-like if:

    n >= 3
    xi + xi+1 == xi+2 for all i + 2 <= n

Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].

## Initial impression
This would be a very simple problem if not for the removal of numbers. It looks like a dynamic programing problem, so perhaps its the type where we work backwards over the array. 

Perhaps we can work L to R working with a set
Because for a fibbonacci sequence, once the first two values are established, the sequence is already determined, it can not change. So for this problem we are only trying to find the first two items that make the longest seq.

Check arr[i] + arr[i+1:] > arr[-1] if true return count because there can be no more sequences starting past i
Check arr[i] + arr[i+1:] is in set(arr):
True, start to construct the sequence, checking each time if the next part is in the set.
False, look for another pair

This logic works and has a middle of the road Runtime for the problem, I was expecting it to go over and require refinement as it is somewhat of a brute force method.

## Learning points
One of the fastest solutions for today used dynamic programming and a method that I had not encountered before, xrange(). This was a memory optimized version of range in a previous version of python, integrated into range in python3.
They define a defaultdict(lambda: 2) which is fun because it defaults the values of any new keys to the result of the lambda.
The code was optimized, but the logic was not very different from my initial impression.