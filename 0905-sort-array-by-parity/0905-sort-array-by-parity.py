class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # i=0
        # ans=[]
        # res=[]
        # while i<len(nums):
        #     if nums[i]%2==0:
        #         ans.append(nums[i])
        #     else:
        #         res.append(nums[i])
        #     i+=1
        # n=len(ans)
        # ans[n:]=res
        # return ans
        i=0
        n=len(nums)
        for j in range(n):
            if nums[j]%2==0:
                nums[i],nums[j]=nums[j],nums[i]
            
                i+=1 
        return nums