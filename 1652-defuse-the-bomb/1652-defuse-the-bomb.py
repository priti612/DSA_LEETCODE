class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        
        if k==0:
            ans=[0]*n
            return ans
        
        ans=[0]*n
        for i in range(n):
            sm=0
            if k>0:
                for j in range(1,k+1):
                    sm+=code[(i+j)%n]
            else:
                for j in range(1,abs(k)+1):
                    sm+=code[(i-j)%n]
            ans[i]=sm
        return ans

            

            