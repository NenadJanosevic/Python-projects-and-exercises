class treeNode:
    def __init__(self,val,left = None ,right = None):
        self.val = val
        self.right = None
        self.left = None


class Soulution(object):

    def isBalnaced(self,root:treeNode):
        def dfs(node):
            if not node:
                return [True,0]
            
            left = dfs(node.left)
            right = dfs(node.right)
            balance = False
            if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
                balance = True
            
            
            return [balance,1 + max(left[1] ,right[1])]
        
        return dfs(root)
                
           
            
root = treeNode(1)
root.left = treeNode(2)
root.right = treeNode(2)
root.left.left = treeNode(3)
root.left.right = treeNode(3)
root.left.left.left = treeNode(4)
root.left.left.right = treeNode(4)
x = Soulution()

print(x.isBalnaced(root))
            
