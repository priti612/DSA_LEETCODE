class Solution:
    def goodDaysToRobBank(self, s: List[int], time: int) -> List[int]:
        n=len(s)
        suff=[0]*n
        pre=[0]*n
        ans=[]
        for i in range(1,n):
            if s[i]<=s[i-1]:
                suff[i]=suff[i-1]+1
        for i in range(n-2,-1,-1):
            if(s[i]<=s[i+1]):
                pre[i]=pre[i+1]+1
        res=[]
        for i in range(time,n-time):
            if suff[i]>=time and pre[i]>=time:
                ans.append(i)
        return ans
            
            

