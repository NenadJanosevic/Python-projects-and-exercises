from collections import defaultdict

class Solution(object):
    def majoretyElement(self,nums):
        res,count = 0,0

        for n in nums:
            if count == 0:
                res = n 
            if res == n:
                count += 1
            elif res != n:
                count -= 1
        return res




            
nums = [2,2,1,1,1,2,2]
x = Solution()
print(x.majoretyElement(nums))