# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.global_sum = float('-inf')

        def sumTree(root):
            if not root:
                return 0
            left = max(sumTree(root.left), 0)
            right = max(sumTree(root.right), 0)
            cur_sum = root.val + left + right
            self.global_sum = max(cur_sum, self.global_sum)

            return root.val + max(left, right)
        sumTree(root)
        return self.global_sum