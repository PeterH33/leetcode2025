# Feb 22, 2025
## Problem
### Recover a tree from preorder Traversal (Hard)

We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.

## Initial impressions
We are going to be creating a tree from a string. The concept is straight forward conversion of one data type to another, so we must find a pattern that can be read logically. 
The tree always leans left if it is getting its first node.
The dash notation logic appears that we track two dash notation blocks length at a time - a and b 
if b > a  place a left child node, 
if b == a place a right node,
if b < a go up to a previous level and place a right node.
Using this logic I need to track the 'active' levels for efficient back tracking to deal with the b < a case
This is pretty straightforward thinking, and it has code smell, I am rather certain there is some way to optimize this and do the work better.

## Second impression
The previous logic is sound, but the implementation is ugly. Optimization comes from trying to do things in a more linear manner. For a level, we will always add left, unless left exists in which case we add right. We are also only going down one branch at a time in a depth first search manner, so we can keep a plot of the current branch and simply back track to the level that we might need.

## Learned
re.findall allows for the use of capture groups to create lists of tuples that can be easily unrwapped, very helpful