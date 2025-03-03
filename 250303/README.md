# March 2, 2025
## Problem
## Partition Array according to given pivot
You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:

    Every element less than pivot appears before every element greater than pivot.
    Every element equal to pivot appears in between the elements less than and greater than pivot.
    The relative order of the elements less than pivot and the elements greater than pivot is maintained.
        More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. If i < j and both elements are smaller (or larger) than pivot, then pi < pj.

Return nums after the rearrangement.

## Initial impression
This problem should be quite simple, so much so that I am concerned that I am missing something. Simple list comprehension can easily execute on this problem. In other languages it would just be a matter of dropping the values into 3 different arrays and combining them.

But today we try for a one line solution for the fun of it.

## Learning
While the solution presented here is not the fastest, the list comprehension found in Python does make this very simple and readable. The above description would be faster, of breaking it into 3 lists all at the same time because the simple one line solution here does go through nums 3 times.