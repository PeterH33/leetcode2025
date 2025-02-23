# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        premap = {v:i for i,v in enumerate(preorder)}

        def dfs(start, end):
            if start > end:
                return None
            # single node tree, or a leaf
            if start == end:
                return TreeNode(postorder.pop())
            
            # Taking the root off
            root = TreeNode(postorder.pop())
            # furthest right of post is the start of the right half in pre
            rightStart = premap[postorder[-1]]

            root.right = dfs(rightStart, end)
            root.left = dfs(start + 1, rightStart - 1)
            
            return root
        
        # they are the same length, but we are excluding the root from the length
        return dfs(0, len(preorder)-1)