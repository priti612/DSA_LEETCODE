class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        x=m*n
        
        if x!=len(original):
            return []

        return[original[i*n:(i+1)*n] for i in range(m)]