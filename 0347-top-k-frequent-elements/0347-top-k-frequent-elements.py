class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f={}
        for i in nums:
            f[i]=f.get(i,0)+1
        
        st=sorted(f,key=lambda x:f[x], reverse=True)
        return st[:k]



            
