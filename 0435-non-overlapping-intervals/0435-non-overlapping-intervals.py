class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        ct=0
        st=intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]>=st:
                st=intervals[i][1]
            else:
                ct+=1

        return ct
