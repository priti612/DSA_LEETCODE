class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res=[]
        
        def sol(i,temp):
            if i==len(s):
                res.append("".join(temp))
                return
            
            if s[i].isdigit():
                temp.append(s[i])
                sol(i+1,temp)
                temp.pop()
            else:
                
                temp.append(s[i].lower())
                sol(i+1,temp)
                temp.pop()
            
                
                temp.append(s[i].upper())
                sol(i+1,temp)
                temp.pop()

        sol(0,[])
        return res