# Feb 23, 2025
## Problem
### Construct a binary tree from preorder and postorder traversal
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.
#### Constraints

    1 <= preorder.length <= 30
    1 <= preorder[i] <= preorder.length
    All the values of preorder are unique.
    postorder.length == preorder.length
    1 <= postorder[i] <= postorder.length
    All the values of postorder are unique.
    It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.


## Initial impression
For the first time in a bit, this is something I have not encountered. Looking at the examples I understand the preorder and why it does not have enough information to construct the tree, but I am new to the post order. 

There are some patterns, I see the root, and the furthest left and right nodes are placed in good spots. However, some reading on what a post order actually is is required, page 335 of Goodrich et al. 'Data Structures and Algorithms' to the rescue. 

Can be broken down into a recustion of tree blocks splitting the preorder. Post order[-2] will be the right node off the root, so everything between preorder[0] and preorder[where i==postorder[-2]] is left, and everything from preorder[where i==postorder[-2]] till the end or preorder is the right.

## Second impressions
It looks like this can be optimized a bit more given the constraints, and the recursion could be the root method. But it does look like the logic is sound for the recursion. I am not seeing many answers that use another logic. 