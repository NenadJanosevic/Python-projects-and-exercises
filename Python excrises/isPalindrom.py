class Soulution(object):
    def isPalindrom(self,s):
        y = ''
        for i in s:
            if i.isalpha():
                y += i
        y = y.lower()
        return y == y[::-1]



x = Soulution()
word = "A man, a plan, a canal: Panama"
print(x.isPalindrom(word))


