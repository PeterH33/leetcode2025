# March 1, 2025
## Problem
### Apply operations to an array
You are given a 0-indexed array nums of size n consisting of non-negative integers.

You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the following on the ith element of nums:

    If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.

After performing all the operations, shift all the 0's to the end of the array.

    For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].

Return the resulting array.

Note that the operations are applied sequentially, not all at once.

## Initial impression
This appears to be a pretty straightforward problem, perhaps there is some fun way to optimize it outside of simply doing what it says.

## Learning
Surprisingly, moving len(nums) out of the range function and up into an assignment statement improved the runtime by 2ms, and changing an assignment opperation from x = x * n to x *= n improved by 1ms this was just a random experiment on my part.

I have not found a more pleasant or faster way to run this problem (0ms already)