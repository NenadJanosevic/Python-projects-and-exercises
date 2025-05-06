class Solution(object):
    def addBinary(self,a,b):
        res = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i>= 0 or j>= 0 or carry:
            sum = carry

            if i >= 0:
                sum += int(a[i])
                i -= 1
            if j >= 0:
                sum += int(b[j])
                j -= 1
            carry = sum // 2
            res.append(str(sum % 2))
        return ''.join(reversed(res))


x = Solution()
print(x.addBinary("11", "1"))    
print(x.addBinary("1010", "1011"))  
            
