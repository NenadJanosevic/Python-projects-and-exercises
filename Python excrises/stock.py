class Solution(object):
    def maxProfit(self,prices):
        min_price = float('inf')
        max_price  = 0

        for i in prices:
            if i < min_price:
                min_price = i
            else:
                max_price = max(max_price,i - min_price)
        return max_price
        
x = Solution()
y = [7, 1, 5, 3, 6, 4]
print(x.maxProfit(y))
            