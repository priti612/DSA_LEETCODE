class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        eql=[]
        grt=[]
        for i in range(len(nums)):
            if nums[i]>pivot:
                grt.append(nums[i])
            elif nums[i]==pivot:
                eql.append(nums[i])
            else:
                less.append(nums[i])
        return less+eql+grt
