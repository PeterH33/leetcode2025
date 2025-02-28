# Feb 28, 2025
## Problem
### Shortest Common Supersequence
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

## Initial Impression
This question appears a bit too easy, as it is hard I must assume that I am over simplifying it. We are simply trying to find the maximum amount that we can overlap the two strings
as per the example str1 = abac, str2 = cab
 
&nbsp;abac  
cab  
cabac

With this in mind, I would start at the end of the word and just move it in to overlap the other so str1[-1] is the same as str2[0] and then expand the logic. I have a feeling that this logic is too simple and will result in a time overflow.

## Learning
The over sight on my part is that the middle of the strings do not nessisarly need to contain all of the letters for a sequence, test case 'bbbaaaba','bbababbb' = 'bbbaaababbb' showed the flaw in my initial logic. Examining other solutions the answer is to create the longest common substring (the overlap as I initially call it), then derive the shortest from that.

The code here provides a short and readable solution, but it is far from optimized.