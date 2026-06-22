class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp={}
        pre=0
        ct=0
        for i in range(len(nums)):
            pre+=nums[i]
            if pre==k:
                ct+=1
            if pre-k in mp:
                ct+=mp[pre-k]
            mp[pre]=mp.get(pre,0)+1
        return ct
