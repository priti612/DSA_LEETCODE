class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prefix=0
        ct=0
        
        f={0:1}
        for x in nums:
            prefix+=x
            t=prefix-k
            if t in f:
              ct+=f[t]
            f[prefix]=f.get(prefix,0)+1
        return ct

