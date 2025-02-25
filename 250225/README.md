# Feb 25, 2025
## Problem
### Number of Sub-arrays with odd sum 

Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 10^9 + 7.

## Initial impression
Problems like this often deal with prefix sums. And this looks like a math question based off of modulo 2 logic.
We can get the count of odd number sums from the summation of prefix sum % 2. Then add to that the number of even numbers * odd numbers which represents a count of every pair of even and odd. 

## Second Impression / Learning
This logic of odd+=even*odd is very specific to this case, and I would like to actually write out the math behind it when I have more time. Its due to the sum and somewhat binary nature of the problem. 