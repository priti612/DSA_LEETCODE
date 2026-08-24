class Solution:
    def reversePrefix(self, s: str, ch: str) -> str:
        idx=s.find(ch)

        return s[:idx+1][::-1]+s[idx+1:]