class Solution:
    def findRightInterval(self, nums: List[List[int]]) -> List[int]:
        st=[]
        for i in range(len(nums)):
            st.append((nums[i][0],i))
        st.sort()
        ans=[]
        for i in range(len(nums)):
            tg=nums[i][1]
            res=-1
            low=0
            high=len(st)-1
            while low<=high:
                mid=low+(high-low)//2
                if st[mid][0]>=tg:
                    res=st[mid][1]
                    high=mid-1
                               
                else:               
                    low=mid+1
            ans.append(res)
                
                    
        return ans
