# March 2, 2025
## Problem
### Merge Two 2d Arrays by summing values (easy)

You are given two 2D integer arrays nums1 and nums2.

    nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
    nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.

Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

    Only ids that appear in at least one of the two arrays should be included in the resulting array.
    Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be 0.

Return the resulting array. The returned array must be sorted in ascending order by id.

## Initial Impression
I was thinking that there might be a sinple way to do this in one line, an dI still bet that there is, but instead I just wrote out the simple logic for executing a sort, and in the event that the index value of the two numbers is equal, add the sum to the result instead.

The simple answer does run in 0ms as expected, and it is quite readable.