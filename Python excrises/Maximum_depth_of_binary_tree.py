class treeNoode():
    def __init__(self,val = 0,left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class solution(object):
    def maxDepth(self,root):
        if root is None:
            return 0
        else:
            left_dept = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_dept,right_depth) + 1
        
        


root = treeNoode(3)
root.right = treeNoode(20)
root.left = treeNoode(9)
root.left.left = treeNoode(15)
root.left.right = treeNoode(7)



x = solution()
print(x.maxDepth(root))

    