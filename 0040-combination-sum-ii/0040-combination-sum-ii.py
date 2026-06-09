class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        def sol(i,temp,tg):
            if tg==0:
                res.append(temp[:])
                return 
            for j in range(i,len(nums)):
                if i!=j and nums[j]==nums[j-1]:
                    continue 
                if nums[j]>tg:
                    break
                temp.append(nums[j])
                sol(j+1,temp,tg-nums[j])
                temp.pop()



        sol(0,[],target)
        return res