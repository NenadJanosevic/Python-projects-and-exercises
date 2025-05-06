class Solution(object):
    def maxSubArray(self,nums):
        max_sum = float('-inf')
        cur_sum = 0

        for n in range(len(nums)):
            cur_sum += nums[n]
            max_sum = max(cur_sum,max_sum)

            if cur_sum < 0:
                cur_sum = 0
        return max_sum

s = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(nums))
        
