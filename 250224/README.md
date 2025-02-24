# Feb 24, 2025
## Problem
### Most Profitable Path in a Tree

There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at node 0. You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

At every node i, there is a gate. You are also given an array of even integers amount, where amount[i] represents:

    the price needed to open the gate at node i, if amount[i] is negative, or,
    the cash reward obtained on opening the gate at node i, otherwise.

The game goes on as follows:

    Initially, Alice is at node 0 and Bob is at node bob.
    At every second, Alice and Bob each move to an adjacent node. Alice moves towards some leaf node, while Bob moves towards node 0.
    For every node along their path, Alice and Bob either spend money to open the gate at that node, or accept the reward. Note that:
        If the gate is already open, no price will be required, nor will there be any cash reward.
        If Alice and Bob reach the node simultaneously, they share the price/reward for opening the gate there. In other words, if the price to open the gate is c, then both Alice and Bob pay c / 2 each. Similarly, if the reward at the gate is c, both of them receive c / 2 each.
    If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches node 0, he stops moving. Note that these events are independent of each other.

Return the maximum net income Alice can have if she travels towards the optimal leaf node.

## Initial impression
Whew thats a lot of description today!
So, we need to find an optimal path for bob to reach 0 and for Alice to reach some optimal node, this screams depth first search.
Because this is an undirected tree and it might have odd branches I can not assume that Bob starts on the branch that Alice will take. However you can assume that if Alice moves down any of the same path as Bob, given they move the same pace, Bob will take out only half the nodes between point bob and 0 and split the middle node if it is an odd number of nodes. 

This leads me to believe that you can run bobs path first, and remove the values in the first half of the bob path, and half an odd value.

After that just run a depth first search to find the optimal path for alice.

## Second impressions and learning points
Python3 really is helpful sometimes, I rather like the walrus for when it can be used to speed up logic. 
The logic for bobs Path is a bit new to me, but I rather like the way that it handles the recursion path, Alice is pretty standard. This is the sort of problem that I make these notes for so that I can continue learning and refer back to things quickly.