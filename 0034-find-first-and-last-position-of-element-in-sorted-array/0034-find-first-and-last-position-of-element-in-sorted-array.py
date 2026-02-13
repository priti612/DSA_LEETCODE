class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def first(nums,target):
            res=-1
            low,high=0,len(nums)-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    res=mid
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return res
        def last(nums,target):
            res=-1
            low,high=0,len(nums)-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    res=mid
                    low=mid+1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return res
        lb = first(nums, target)
        ub = last(nums, target)
        return [lb, ub]
        


