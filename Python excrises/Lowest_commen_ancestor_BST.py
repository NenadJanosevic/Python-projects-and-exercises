class treeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


        

class solution(object):
    def lowestCommonAncestor(self,root,p,q):
        current = root

        while current:
            if p.val < current.val  and q.val < current.val:
                current = current.left
            elif p.val > current.val  and q.val > current.val:
                current = current.right
            else:
                return current
        
root =  treeNode(6)
root.left = treeNode(2) 
root.right = treeNode(8)
root.left.left = treeNode(0)
root.left.right = treeNode(4)
root.right.left = treeNode(7)
root.right.right = treeNode(9)
root.left.right.left = treeNode(3)
root.left.right.right = treeNode(5)

p = root.left
q = root.right

x = solution()
print(x.lowestCommonAncestor(root,p,q).val)