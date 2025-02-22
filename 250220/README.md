# Feb 20, 2025
## Problem
### Find Unique Binary String
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

## Initial Impressions
This problem appears very simple, we are only looking for a value not in a list of binary strings of a set length. Lets just count! While counting, the first number that is not present is a solution, this method would allow for finding all of the values not present in nums.

## Second impression
I have the feeling that this logic could easily be shorened up even more