class Solution(object):
    def kclosest(self,points,k):

        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        
        return points[:k]
        
x = Solution()
number = [[1,3],[-2,2]] 
print(x.kclosest(number,1))
