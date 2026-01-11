class Solution:
    def solved(self,h):
            st=[]
            max_a=0
            hs=h+[0]
            for i in range(len(hs)):    
                while st and hs[i]<hs[st[-1]]:
                    hh=hs[st.pop()]
                    if not st:
                        w=i
                    else:
                        w=i-st[-1]-1
                    max_a=max(max_a,hh*w)
                st.append(i)
            return max_a
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        maxi=0
        h=[0]*m
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=='1':
                    h[j]+=1
                else:
                    h[j]=0
            maxi=max(maxi,self.solved(h))
        return maxi
        
                    

            