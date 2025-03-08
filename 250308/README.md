# March 8, 2025
## Problem
### Minimum recolors to get K consecutive black blocks

You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

## Initial impression
This is a problem type thatI am still learning, it looks like a sliding window type. Given that k is set, I will attempt to simply move a slice along and find the point with the fewest number of W for a length of k.

## Learning
Using the count method makes the window operation pretty simple, but I am left with a less efficient method than an optimized solution. The optimized solution moves a window a long while tracking the current total in and out of the window under consideration. I would argue that the solution I presented is more readable, but it is certainly less optimized and that difference would grow significantly on a larger sample.