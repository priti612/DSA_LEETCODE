class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr)<2:
            return len(arr)
        ct=0
        up,down=1,1
        mx=1
        for i in range(1,len(arr)):
            if arr[i]>arr[i-1]:
                up=down+1
                down=1
            elif arr[i-1]>arr[i]:
                down=up+1
                up=1
            else:
                up=down=1
                
            mx=max(mx,up,down)            
        return mx