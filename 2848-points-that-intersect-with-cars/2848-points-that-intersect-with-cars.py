class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        ans=[]
        for st,ed in nums:
            for y in range(st,ed+1):
                ans.append(y)
        ans=list(ans)
        ans=set(ans)
        return len(ans)