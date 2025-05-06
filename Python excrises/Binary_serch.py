class Soulution(object):
    def search(self,nums,target):
                nums = sorted(nums)
                (left,right) = (0, len(nums) - 1)
                while left <= right:
                    mid = (left + right) // 2 
                    if target == nums[mid]:
                            return nums[mid]
                    elif target < nums[mid]:
                            right = mid - 1
                    
                    else:
                            left = mid + 1
                return -1
                        
                 
               
                
                



x = Soulution()
nums = [-1,0,3,5,9,12]
target = 9
print(x.search(nums,target))