class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp={0:1}
        pre=0
        ct=0

        for i in range(len(nums)):
            pre+=nums[i]
            rem=pre%k
                
            if rem in mp:
                ct+=mp[rem]
            mp[rem]=mp.get(rem,0)+1
        return ct
