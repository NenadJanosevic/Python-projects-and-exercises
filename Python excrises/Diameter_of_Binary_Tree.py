class TreeNode:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def  diameterofBinaryTree(self,root):
        self.max_diameter = 0
        def dfs(node):
            if not node:
                return 0
            left_dfs = dfs(node.left)
            right_dfs = dfs(node.right)
            self.max_diameter = max(self.max_diameter, left_dfs + right_dfs)

            return max(left_dfs,right_dfs) + 1
        dfs(root)
        return self.max_diameter


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

x = Solution()
print(x.diameterofBinaryTree(root))
