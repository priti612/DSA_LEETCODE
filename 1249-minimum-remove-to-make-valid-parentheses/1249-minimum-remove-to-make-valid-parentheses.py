class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans=[]
        op=0
        for val in s:
            if val=='(':
                op+=1
                ans.append(val)
            elif val==')':
                if op>0:
                    op-=1
                    ans.append(val)
            else:
                ans.append(val)
        res=[]
        ct=0
        
        for val in ans[::-1]:
            if val==')':
                ct+=1
                res.append(val)
            elif val=='(':
                if ct>0:
                    ct-=1
                    res.append(val)
            else:
                res.append(val)
        return "".join(res[::-1])

