class Soulution(object):
    def floodFile(self,image,sr,sc,color):
        
        starting = image[sr][sc]

        self.dfs(image,sr,sc,color,starting)

        return image
        
    def dfs(self,image,sr,sc,color,starting):

        if sr < 0 or sr > len(image) - 1 or sc < 0 or sc > len(image[0]) -1 or image [sr][sc] == color or image[sr][sc] != starting:
            return
        
        image[sr][sc] = color
        self.dfs(image,sr + 1, sc, color, starting)
        self.dfs(image,sr - 1, sc, color, starting)
        self.dfs(image,sr, sc + 1, color, starting)
        self.dfs(image,sr, sc - 1, color, starting)


image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
sr = 1 
sc = 1 
color = 2
x = Soulution()
print(x.floodFile(image,sr,sc,color))
        

