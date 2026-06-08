class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        
        def sub(i,temp):
            
            res.append(temp[:])
            for j in range(i,len(nums)):
                temp.append(nums[j])
                sub(j+1,temp)
                temp.pop()
        temp=[]
        sub(0,temp)
        return res