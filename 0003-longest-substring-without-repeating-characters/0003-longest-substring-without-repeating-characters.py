class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp={}
        low=0
        maxi=0
        for i ,val in enumerate(s):
            if val in mp and mp[val]>=low:
                low=mp[val]+1
            mp[val]=i
            maxi=max(maxi,i-low+1)
        return maxi

