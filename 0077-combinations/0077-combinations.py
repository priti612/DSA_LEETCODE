class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        nums=list(range(1,n+1))
        def sol(i,k,temp):
            if k==0:
                res.append(temp[:])
                return
            if i==len(nums):
                return
            temp.append(nums[i])
            sol(i+1,k-1,temp)
            temp.pop()
            sol(i+1,k,temp)

        sol(0,k,[])
        return res
