import re

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f'TreeNode val={self.val}'


class Solution:
    def recoverFromPreorder(self, traversal) -> TreeNode:
        # Using a dictionary we can automatically keep track of the level of the active nodes
        dashMap = {}   

        # Need to seed the root location in the map so that we do not need to do any odd logic in the for loop below
        first_num = re.search(r'\d+', traversal)
        dashMap[0] = TreeNode(int(first_num.group()))

        # Parse out the string using capture groups
        s = re.findall(r'(-+)(\d+)', traversal)

        for dash, num in s:
            dashCount = len(dash)
            # have to convert the string to an int
            num = int(num)
            newNode = TreeNode(num)
            # Get the currently tracked active node that lines up with the dash level -1
            parentNode = dashMap[dashCount - 1]
            # set the node, left to right
            if not parentNode.left:
                parentNode.left = newNode
            elif not parentNode.right:
                parentNode.right = newNode
            # Place the most recent node onto the active map at its level
            dashMap[dashCount] = newNode

        return dashMap[0]