# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, s):
            if not node: return 0
            if not node.left and not node.right:
                nonlocal ans
                s += str(node.val)
                ans += int(s)
                return
            
            s += str(node.val)
            dfs(node.left, s)
            dfs(node.right, s)
                
        
        dfs(root, "")
        return ans