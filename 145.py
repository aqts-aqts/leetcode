# Binary Tree Postorder Traversal
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def postorderTraversal(self, root):
        traversal = []
        def postorder(node):
            if node is None: return
            postorder(node.left)
            postorder(node.right)
            traversal.append(node.val)
        postorder(root)
        return traversal