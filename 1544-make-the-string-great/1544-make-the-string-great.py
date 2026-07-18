class Solution:
    def makeGood(self, s: str) -> str:
        st=[]
        for i in range(len(s)):
            if st and abs(ord(s[i])-ord(st[-1]))==32:
                st.pop()
            else:
                st.append(s[i])
        return "".join(st)