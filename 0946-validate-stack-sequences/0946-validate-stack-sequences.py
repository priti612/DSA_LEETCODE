class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st=[]
        pp=0
        sp=-1
        for i in range(len(pushed)):
            st.append(pushed[i])
            while st and st[-1]==popped[pp]:
                st.pop()
                pp+=1
            if pp==len(popped):
                return True
        return False
        
        

            