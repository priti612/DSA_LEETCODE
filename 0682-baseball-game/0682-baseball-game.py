class Solution:
    def calPoints(self, ops: List[str]) -> int:
        st=[]
        
        for ps in ops:
            if ps=='C':
                if st:
                    st.pop()
            elif ps=='D':
                
                st.append(st[-1]*2)
            elif ps=='+':
                
                st.append(st[-1]+st[-2])
            else:
                st.append(int(ps))
        return sum(st)
        
        