class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        r=-1
        n=len(arr)
        
        for i in range(n-1,-1,-1):
            arr[i],r=r,max(arr[i],r)
        return arr