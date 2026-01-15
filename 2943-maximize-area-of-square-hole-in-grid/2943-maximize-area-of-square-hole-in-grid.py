class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        max_hbar=1
        max_vbar=1
        curr=1
        for i in range(1,len(hBars)):
            if hBars[i]-hBars[i-1]==1:
                curr+=1
            else:
                curr=1
            max_hbar=max(max_hbar,curr)
        curr_v=1
        for i in range(1,len(vBars)):
            if vBars[i]-vBars[i-1]==1:
                curr_v+=1
            else:
                curr_v=1
            max_vbar=max(max_vbar,curr_v)
        s=min(max_hbar,max_vbar)+1
        return s*s
        

