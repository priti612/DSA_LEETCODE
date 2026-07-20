class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        st=[]
        res=[]
        def sol(op,cl):
            if op==cl==n:
                res.append("".join(st))
                return
            if op<n:
                st.append('(')
                sol(op+1,cl)
                st.pop()
            if cl<op:
                st.append(')')
                sol(op,cl+1)
                st.pop()

        sol(0,0)
        return res