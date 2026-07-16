class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        inc=1
        dec=1
        mx=1
        for i in range(1,len(arr)):
            if arr[i-1]>arr[i]:
                dec=inc+1
                inc=1
            elif arr[i-1]<arr[i]:
                inc=dec+1
                dec=1
            else:
                inc=1
                dec=1
            mx=max(dec,inc,mx)
        return mx