class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def sub(i,temp):
            if temp[:] not in res:
                res.append(temp[:])
            for j in range(i,len(nums)):
                if j!=i and nums[j]==nums[j-1]:
                    continue 
                temp.append(nums[j])
                sub(j+1,temp)
                temp.pop()
        sub(0,[])
        return res