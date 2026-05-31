class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ct=0
        
        for i in range(len(nums)):
            st=int(str(nums[i])[0])
            for j in range(i+1,len(nums)):
                lst=nums[j]%10
                if math.gcd(st,lst)==1:
                    ct+=1
                
        return ct