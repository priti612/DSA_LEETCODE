class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        ans=[]
        for i in d:
            if d[i]>1:
                ans.append(i)
        return ans