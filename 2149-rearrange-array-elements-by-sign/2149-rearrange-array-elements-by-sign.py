class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans=[]
        pos=[i for i in nums if i>0]
        neg=[i for i in nums if i<0]
        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans