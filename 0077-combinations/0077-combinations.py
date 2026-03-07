class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return list(combinations(range(1,n+1),k))
        res=[]
        nums=[i for i in range(1,n+1)]
        def com(i,temp,k):
            if k==0:
                res.append(temp[:])
                return
            if i==len(nums):
                return
            temp.append(nums[i])
            com(i+1,temp,k-1)
            temp.pop()
            com(i+1,temp,k)
        com(0,[],k)
        return res