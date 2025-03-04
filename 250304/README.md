# March 4, 2025
## Problem
### Check if number is a sum of powers of three (Medium)

Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.

## Initial impression

This problem appears to either be a math problem or use a table to quickly check for possible answers. For the fun of it I am just going to go down a programatic path. Our constraint is 1 <= n <= 10^7 so that limits us to 3^14 as the highest value as 3^15 is over 10^7, or we can use an organic cap of whatever n is. And then simply check for a subset sum.

## Learning

Learned a little about bitmasking for the subset sum problem and integrated that method alongside a table of powers of 3. The solution works and is fun. Trying to work through the logic of this I am a bit surprised that this solution does not run into some sort of overflow error, just pushing the limit of it, it works better for smaller values than what is used here.

A far simpler solution is to do repeated floor division of the value n by 3. If the remainder is ever 2, return false, otherwise return True when the value hits 0.