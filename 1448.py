# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
            
        def diveTree(node, good_vals, curr_biggest):
            if not node:
                return 0
            if node.val >= curr_biggest:
                curr_biggest = node.val
                good_vals.append(node.val)
            if not node.left and not node.right:
                return 0
            diveTree(node.left, good_vals, curr_biggest)
            diveTree(node.right, good_vals, curr_biggest)

        good_vals = [root.val]
        curr_biggest = root.val
        diveTree(root, good_vals, curr_biggest)
        return len(good_vals)-1