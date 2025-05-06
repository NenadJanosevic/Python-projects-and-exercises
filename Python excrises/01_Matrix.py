from collections import deque

class Solution(object):
    def updateMatrix(self,mat):
        #row right
        row = len(mat)
        #colum down 
        col = len(mat[0])
        queue = deque()
        distanc = []
        for _ in range(row):
            distanc.append([float('inf')] * col)
    
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    distanc[i][j] = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while queue:
            x,y = queue.popleft()

            for dx,dy in directions:
                nx ,ny = x+dx , y + dy
                if 0 < nx < row and 0 <= ny < col:
                    if distanc[nx][ny] > distanc[x][y] +1:
                        distanc[nx][ny] = distanc[x][y] +1
                        queue.append((nx,ny))
        return distanc
    
s = Solution()
mat = [[0,0,0],[0,1,0],[1,1,1]]
print(s.updateMatrix(mat))


        





















s = Solution()
mat = [[0,0,0],[0,1,0],[0,0,0]]
print(s.updateMatrix(mat))