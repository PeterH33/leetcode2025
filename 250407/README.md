# April 7, 2025
## Problem
### Partition Equal Subset Sum
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

## Initial Impression
It appears that we can simply sort the array, then move along the resulting array and see if there is a point where left and right are equal. Sadly this does not work for sets where the pattern is 1,1,2,2.