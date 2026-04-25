class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        mp={}
        ct=0
        n=len(nums)
        need=n*(n-1)//2
        for i,num in enumerate(nums):
            pre=num-i
            if pre in mp:
                ct+=mp[pre]
            mp[pre]=mp.get(pre,0)+1
        return need-ct