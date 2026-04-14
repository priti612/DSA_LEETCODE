class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        ans=[]
        for i in s.split():
            if i.isdigit():
                ans.append(int(i))
        # res=int(ans)
        for i in range(len(ans)-1):
            if ans[i]>=ans[i+1]:
                return False
        return True