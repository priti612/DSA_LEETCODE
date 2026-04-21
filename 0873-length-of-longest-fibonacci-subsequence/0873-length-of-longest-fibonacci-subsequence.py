class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        if len(arr)<3:
            return 2
        s=set(arr)
        maxi=0
        ct=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                a=arr[i]
                b=arr[j]
                ct=2
                while (a+b) in s:
                    a,b=b,a+b
                    ct+=1
                    if ct>=3:
                        maxi=max(ct,maxi)
        return maxi