class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ct=0
        mp={0:1}
        pre=0
        for num in nums:
            if num%2!=0:
                pre+=1
            if pre-k in mp:
                ct+=mp[pre-k]
            mp[pre]=mp.get(pre,0)+1
        return ct
