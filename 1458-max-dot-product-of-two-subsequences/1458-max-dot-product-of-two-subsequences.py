class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        # def solve(i,j):
        #     n=len(nums1)
        #     m=len(nums2)
        #     if i==n or j==m:
        #         return float('-inf')
        #     val=nums1[i]*nums2[j]
        #     takeij =val+max(0,solve(i+1,j+1))
        #     takei=solve(i,j+1)
        #     takej=solve(i+1,j)
        #     return max(val,takeij,takei,takej)
        
        # n=len(nums1)
        # m=len(nums2)
        # return solve(0,0)

        n=len(nums1)
        m=len(nums2)

        t=[[-math.inf]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                val=nums1[i-1]*nums2[j-1]
                t[i][j]=max(val,val+t[i-1][j-1],t[i-1][j],t[i][j-1])
        return t[n][m]
