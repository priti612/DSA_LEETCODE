class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ct=0
        s=set(nums)
        for num in s:
            maxi=0
            if num-1 not in s:
                curr=num
                maxi+=1
                while curr+1 in s:
                    maxi+=1
                    curr+=1
                ct=max(ct,maxi)
        return ct 

        
