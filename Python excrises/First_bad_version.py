def isBadVersion(version):
    bad_version = 4
    return version >= bad_version


class Solution():
       
    def firstbadversion(self,n):
        L = 1
        R = n
        while L < R:
           m = (L + R) // 2
           if isBadVersion(m):
            R = m
           else: 
            L = m + 1
        return L
    def checkVersion(self, version):
        return isBadVersion(version)

x = Solution()
print(x.checkVersion(1))
print(x.checkVersion(2))
print(x.checkVersion(3))
print(x.checkVersion(4))
print(x.checkVersion(5))
print(x.checkVersion(6))
print(x.checkVersion(7))
print(x.checkVersion(8))
            
