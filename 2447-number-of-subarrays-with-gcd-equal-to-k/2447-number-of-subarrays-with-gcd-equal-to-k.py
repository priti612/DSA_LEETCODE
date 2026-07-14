class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        ct=0
        n=len(nums)
        for i in range(n):
            curr=0
            for j in range(i,n):
                curr=math.gcd(curr,nums[j])
                if curr==k:
                    ct+=1
                elif curr<k:
                    break
        return ct
            
