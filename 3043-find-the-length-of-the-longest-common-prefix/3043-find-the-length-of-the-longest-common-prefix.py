class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        ct=0
        hashset=set()
        for val in arr1:
            while val>0:
                hashset.add(val)
                val//=10
        for val in arr2:
            while val>0:
                if val in hashset:
                    ct=max(ct,len(str(val)))
                val//=10
        return ct
