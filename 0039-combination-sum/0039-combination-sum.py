class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        def sol(i,temp,tg):
            if tg==0:
                res.append(temp[:])
                return
            if i>=len(nums) or tg<0:
                return
            
            for j in range(i,len(nums)):
                if nums[j]>tg:
                    break
                temp.append(nums[j])
                sol(j,temp,tg-nums[j])
                temp.pop()

        sol(0,[],target)
        return res
            
        