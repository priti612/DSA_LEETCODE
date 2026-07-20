class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res=[]
        def sol(idx,subset):
            if idx==len(s):
                res.append(list(subset))
                return
            
            for i in range(idx,len(s)):
                sub=s[idx:i+1]
                if sub==sub[::-1]:
                    subset.append(sub)
                    sol(i+1,subset)
                    subset.pop()
        sol(0,[])
        return res