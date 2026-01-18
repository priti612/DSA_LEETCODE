class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ct=0
        summ=0
        pre={0:1}
        for num in nums:
            summ+=num
            t=summ-k
            if t in pre:
                ct+=pre[t]
            pre[summ]=pre.get(summ,0)+1
        return ct
        