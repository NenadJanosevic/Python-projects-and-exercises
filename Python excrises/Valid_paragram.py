class solution(object):
    def isAnagram(self,s,t):
        return sorted(s) == sorted(t)
        
        

s = "anagram"
t = "nagara"
x = solution()
y = x.isAnagram(s,t)

print(y)