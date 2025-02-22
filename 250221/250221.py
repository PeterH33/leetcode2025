class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    # We can speed up the find method dramatically by keeping a set of all the numbers in the tree as the tree is repaired.
    elementSet = set()
    
    def __init__(self, root: Optional[TreeNode]):
        # Start at the root and recursive add in values
        self.elementSet.clear()
        self.root = root
        self.repair(0, root)
        # print('elements', self.elementSet)

    def repair(self, setValue, currentNode):
        # print(currentNode.val, setValue)
        self.elementSet.add(setValue)
        currentNode.val = setValue
        if currentNode.left:
            self.repair(2*setValue+1, currentNode.left)
        if currentNode.right:
            self.repair(2*setValue+2, currentNode.right)

    def find(self, target: int) -> bool:
        if target in self.elementSet:
            return True
        else:
            return False