class Solution(object):
    def insert(self,intervals,newInterval):
        res = []
         #interval = [[1,3],[6,9]]
         # newInterval = [2,5]

        for i in intervals:
            if newInterval[1]<i[0]:
                res.append(newInterval)
                newInterval = i
            elif newInterval[0]>i[1]:
                res.append(i)
            else:
                newInterval[0] = min(newInterval[0],i[0])
                newInterval[1] = max(newInterval[1],i[1])
        res.append(newInterval)
        return res
    

    

s = Solution()
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(s.insert(intervals,newInterval))