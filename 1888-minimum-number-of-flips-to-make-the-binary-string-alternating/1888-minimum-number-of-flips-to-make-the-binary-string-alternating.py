class Solution:
    def minFlips(self, s: str) -> int:
        n=len(s)
        arr1=[]
        arr2=[]
        s=s+s
        for i in range(len(s)):
            arr1.append('1' if i%2==0 else '0')
            arr2.append('0' if i%2==0 else '1')
        l=0
        res=float('inf')
        diff1=0
        diff2=0
        for i in range(len(s)):
            
            if s[i]!=arr1[i]:
                diff1+=1
            if s[i]!=arr2[i]:
                diff2+=1
            if i-l+1>n:
                if s[l]!=arr1[l]:
                    diff1-=1
                if s[l]!=arr2[l]:
                    diff2-=1
                l+=1
            if i-l+1==n:
                res=min(res,diff1,diff2)
        return res
