class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums1)
        m=len(nums2)
        st=[]
        res=[]
        nge={}
        for i in reversed(nums2):
                while st and st[-1]<i:
                    st.pop()
                if st:
                    nge[i]=st[-1]
                else:
                    nge[i]=-1
                st.append(i)
        for i in nums1:
            res.append(nge[i])
        return res

