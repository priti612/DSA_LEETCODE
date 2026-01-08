class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums1)
        m=len(nums2)
        res=[-1]*n
        st=[]
        fre={}
        for i in range(m-1,-1,-1):
            curr=nums2[i]
            while st and st[-1]<=nums2[i]:
                st.pop()
            if not st:
                fre[curr]=-1
            else:
                fre[curr]=st[-1]
            st.append(curr)
        return [fre[i] for i in nums1]
        