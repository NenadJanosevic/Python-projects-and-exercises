from collections import defaultdict

class Solution(object):
    def longestPalindrom(self,s):
        map = defaultdict(int)
        res = 0

        for chr in s:
            map[chr] += 1
            if map[chr] % 2 == 0:
                res += 2

        for i in map.values():
            if i % 2:
                res += 1
                break

        return res


x = Solution()
s = "abccccdd"
print(x.longestPalindrom(s))