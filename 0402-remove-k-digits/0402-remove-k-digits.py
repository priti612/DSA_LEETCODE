class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        ct=0
        for nm in num:
            while k>0 and st and st[-1]>nm:
                st.pop()
                k-=1
            st.append(nm)
        while k>0:
            st.pop()
            k-=1
        r="".join(st).lstrip('0')
        return r if r!="" else '0'
