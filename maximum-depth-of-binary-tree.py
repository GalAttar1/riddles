# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def defs(root, depth) -> int:
            if root is None: return depth
            left = int(defs(root.left, depth + 1))
            right = int(defs(root.right, depth + 1))
            return max(left, right)

        return defs(root, 0)
