class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def sol(i,temp):
            if temp[:] not in res:
                res.append(temp[:])
            for j in range(i,len(nums)):
                if j!=i and nums[j]==nums[j-1]:
                    continue 
                
                temp.append(nums[j])
                sol(j+1,temp)
                temp.pop()
                


        sol(0,[])
        return res