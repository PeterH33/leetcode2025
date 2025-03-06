# March 6, 2025
## Problem
### Find missing and repeated values

You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

## Initial impression
This is a pretty simple problem to solve, so the goal will be in solving it in the most efficient manner, Dropping all of the values into a dictionary and then finding the values that are 0 and 2 would work. It would also work to itterate through the grid, watching for the double via a dictionary, and carring a running total, then subtract that running total from the sum of 1 -> n to get the missing value. 

## Learning points
Well this does certainly go pretty fast, ariving at the solution in 3ms when the graph of submissions is listing the minimum as 6ms, but someone is doing it in 0, so it can be even faster. Attempting to change the list comprehension that converts the 2d grid to a 1d list for analysis did not speed it up, can not seem to get below 3ms. But this does run in O(n) time as we have to look at all the items in the list just the once.