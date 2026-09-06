class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        ans=[]
        def sol(i,res):
            
            if i==len(digits):
                ans.append(res)
                return
            for ch in mp[digits[i]]:
                sol(i+1,res+ch)
            
            

        sol(0,"")
        return ans
