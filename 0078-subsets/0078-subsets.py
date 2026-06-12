class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def sol(i,temp):
            res.append(temp[:])
            for j in range(i,len(nums)):
                temp.append(nums[j])
                sol(j+1,temp)
                temp.pop()
        sol(0,[])
        return res