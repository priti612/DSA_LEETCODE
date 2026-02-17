class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        def findnse(arr):
            n=len(arr)
            st=[]
            nse=[n]*n
            for i in range(n-1,-1,-1):
                while st and arr[st[-1]]>=arr[i]:
                    st.pop()
                if st:
                    nse[i]=st[-1]
                st.append(i)
            return nse
        def findpse(arr):
            n=len(arr)
            st=[]
            res=[-1]*n
            for i in range(n):
                while st and arr[st[-1]]>arr[i]:
                    st.pop()
                if st:
                    res[i]=st[-1]
                
                st.append(i)
            return res
        nse=findnse(arr)
        pse=findpse(arr)
        tot=0
        mod=10**9+7
        for i in range(len(arr)):
            l=i-pse[i]
            r=nse[i]-i
            tot+=r*l*arr[i]
        return tot%mod

