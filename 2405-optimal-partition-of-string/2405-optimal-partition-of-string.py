class Solution:
    def partitionString(self, s: str) -> int:
        f=set()
        res=1
        for ch in s:
            if ch in f:
                res+=1
                f.clear()
            f.add(ch)
        return res
