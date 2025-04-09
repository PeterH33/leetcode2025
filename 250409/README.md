# April 9, 2025
## Problem
### Minimum Operations to Make Array Values Equal to K
You are given an integer array nums and an integer k.

An integer h is called valid if all values in the array that are strictly greater than h are identical.

For example, if nums = [10, 8, 10, 8], a valid integer is h = 9 because all nums[i] > 9 are equal to 10, but 5 is not a valid integer.

You are allowed to perform the following operation on nums:

    Select an integer h that is valid for the current values in nums.
    For each index i where nums[i] > h, set nums[i] to h.

Return the minimum number of operations required to make every element in nums equal to k. If it is impossible to make all elements equal to k, return -1.

## Initial impression
I won't lie, that was a strange description for the problem, perhaps they are trying to find ways to trip up AI generated responses.
The problem is very simple (it is ranked easy after all).
If there is any value less than k, return -1
Then simply count the number of unique values that are not k in nums and return that value.

## Learning
A good optimization is to combine the first step with the rest of the logic by adding values to the set as you read the list once.