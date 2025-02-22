# Feb 21, 2025
## Problem
### Find elements in a contaminated binary tree.
Given a binary tree with the following rules:

    root.val == 0
    For any treeNode:
        If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
        If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2

Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

Implement the FindElements class:

    FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
    bool find(int target) Returns true if the target value exists in the recovered binary tree.

## Initial impression
When looking at this problem it seems like we can increace the speed by placing each value into a set as we encounter them.

## Lessons learned
Oddly, I have not dealt with classes and methods in python up to this point, as such the way that python handles self was rather new.
The way that elementSet is listed as a component of the class and not created in init creates a behavior where the set persists between different instances of the class, messing with the test cases. As an experimental fix, instead of moving elementSet, self.elementSet.clear() is called at the begining of init. The behavior works, but is inefficient.