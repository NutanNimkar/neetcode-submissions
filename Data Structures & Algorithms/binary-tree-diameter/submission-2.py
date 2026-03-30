# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.global_max = 0
        self.cur_max = 0

        def dfs(root):
            if not root: 
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.cur_max = left + right
            self.global_max = max(self.global_max, self.cur_max)
            return 1 + max(left, right)
        dfs(root)
        return self.global_max