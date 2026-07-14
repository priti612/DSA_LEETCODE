class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        maxi=max(nums)
        s=set(nums)
        ans=0
        for i in range(1,maxi+1):
            curr=0
            for j in range(i,maxi+1,i):
                if j in s:
                    curr=math.gcd(curr,j)
                    if curr==i:
                        ans+=1
                        break
        return ans