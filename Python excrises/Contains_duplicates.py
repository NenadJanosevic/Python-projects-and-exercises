class Solution(object):
    def containesDuplicate(self,nums):
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False



S = Solution()
nums = [1,2,3,1]
print(S.containesDuplicate(nums))
        

        
            
        
    