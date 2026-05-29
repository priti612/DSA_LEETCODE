class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        ct=0
        for i in nums1:
            if i in nums2:
                ct+=1
        ans.append(ct)
        ct=0
        for i in nums2:
            if i in nums1:
                ct+=1
        ans.append(ct)
        return ans

        
