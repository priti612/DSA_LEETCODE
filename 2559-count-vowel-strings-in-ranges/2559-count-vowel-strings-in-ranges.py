class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vol={'a','e','i','o','u'}
        n=len(words)
        p=[0]*(n+1)
        for i,j in enumerate(words):
            val=1 if(j[0] in vol and j[-1] in vol) else 0
            p[i+1]=p[i]+val
        ans=[]
        for l,r in queries:
            ans.append(p[r+1]-p[l])
        return ans
        
            
