class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first(nums,targ):
            res=-1
            low=0
            high=len(nums)-1
            while low<=high:
                mid=low+(high-low)//2
                if nums[mid]==targ:
                    res=mid
                    high=mid-1
                elif nums[mid]<targ:
                    low=mid+1
                else:
                    high=mid-1
            return res
        def second(nums,targ):
            res=-1
            low=0
            high=len(nums)-1
            while low<=high:
                mid=low+(high-low)//2
                if nums[mid]==targ:
                    res=mid
                    low=mid+1
                elif nums[mid]<targ:
                    low=mid+1
                else:
                    high=mid-1
            return res


        lb=first(nums,target)
        ub=second(nums,target)
        return[lb,ub]
        