class Soulution():
    def invertTree(self,root):
        st = [root]
        while len(st) > 0:
            node = st.pop()
            if node != None:
                hold = node.left
                node.left = node.right
                node.right = hold

                st.append(node.left)
                st.append(node.right)

        return root
    

x = Soulution()
arr = [4, 2, 7, 1, 3, 6, 9]
print(x.invertTree(arr))