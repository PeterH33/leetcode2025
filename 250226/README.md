# Feb 26, 2025
## Problem
### Maximum Absolute Sum of Any Subarray

You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

    If x is a negative integer, then abs(x) = -x.
    If x is a non-negative integer, then abs(x) = x.

## Initial Impression
Any time that a problem asks for something dealing with sub arrays, I think about recursion and dynamic programming. This specific case is new to me. It appears that we need to track a min and a max at the same time.

## Learning points
This problem introduces Kadane's Algorithm to me for doing the problem in O(n) time. An interesting algorithm that bears looking up.