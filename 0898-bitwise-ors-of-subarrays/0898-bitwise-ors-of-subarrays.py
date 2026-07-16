class Solution:
    def subarrayBitwiseORs(self, nums: List[int]) -> int:
        
        ans=set()
        cur=set()
        for v in nums:
            curr={v|x for x in cur}
            curr.add(v)
            ans.update(curr)
            cur=curr
        return len(ans)
