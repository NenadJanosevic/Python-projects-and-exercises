class Solution(object):
    def canConstruct(slef,ransomNote,magazine):
        counter = {}
        
        for c in magazine:
            counter[c] = 1 +counter.get(c,0)
        for c in ransomNote:
            if c not in counter:
                return False
            elif counter[c] == 1:
                del counter[c]
            else:
                counter[c] -= 1
        return True
    
x = Solution()
a = 'aa'
b = 'aab'

print(x.canConstruct(a,b))

                