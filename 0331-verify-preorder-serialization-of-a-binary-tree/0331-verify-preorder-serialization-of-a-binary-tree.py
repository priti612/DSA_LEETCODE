class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if not preorder:
            return True
        d=preorder.split(",")
        st=[]
        for i in d:
            st.append(i)
            while len(st)>=3 and st[-1]=='#' and st[-2]=='#'and st[-3]!='#':
                st.pop()
                st.pop()
                st.pop()
                st.append('#')
        return len(st)==1 and st[0]=='#'
