class Solution:
    def findTargetSumWays(self, arr: List[int], diff: int) -> int:
        # def subset(arr,tag):
        def countsub(arr,summ):
            n=len(arr)
            t=[[0]*(summ+1) for _ in range(n+1)]
            t[0][0]=1
            for i in range(1,n+1):
                for j in range(summ+1):
                    if arr[i-1]<=j:
                        t[i][j]=t[i-1][j-arr[i-1]] + t[i-1][j]
                    else:
                        t[i][j]=t[i-1][j]
            return t[n][summ]
        n=len(arr)
        s1=sum(arr)
        sum_s1=(diff+s1)//2
        if (diff +s1) % 2 != 0 or abs(diff)>s1:
            return 0
        return countsub(arr,sum_s1)
        