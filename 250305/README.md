# March 5, 2025
## Problem
### Count total number of colored cells
There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer n, indicating that you must do the following routine for n minutes:

    At the first minute, color any arbitrary unit cell blue.
    Every minute thereafter, color blue every uncolored cell that touches a blue cell.

## Initial impression
This must be a math problem, considering the rather large value of n <= 10^5.
On every loop of the problem, 4 more than the amount last added is added to the current total.

The sum of the first n-1 integers is ((n-1)n)/2  
we add 1 for the starting amount at a value of 1 giving  
1 + 4*(((n-1)n)/2)  
Which simplifies to  
1 + 2 * (n-1) * n
