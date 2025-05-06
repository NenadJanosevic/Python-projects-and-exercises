class Solution(object):
    def climbingStairs(self,n):
        if n <= 2:
            return n
    
        prev = 1
        cur = 2
        for i in range(3,n+1):
            new_cur = prev + cur
            prev = cur
            cur = new_cur
        return prev
        
x = Solution()
print(x.climbingStairs(5))
