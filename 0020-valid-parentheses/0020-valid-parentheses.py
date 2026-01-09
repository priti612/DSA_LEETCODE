class Solution:
    def isValid(self, s: str) -> bool:
        b=["(","[","{"]
        st=[]
        for i in s:
            if i in b:
                if i=='(':
                    st.append(')')
                elif i=='{':
                    st.append('}')
                elif i=='[':
                    st.append(']')
            else:
                if not st:
                    return False
                if st.pop()!=i:
                    return False
        return len(st)==0
