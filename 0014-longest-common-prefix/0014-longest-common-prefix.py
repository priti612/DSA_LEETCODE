class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i=0
        n=len(strs)
        mini=float('inf')
        for s in strs:
            if len(s)<mini:
                mini=len(s)
        while i<mini:
            for s in strs:
                if s[i]!=strs[0][i]:
                    return strs[0][:i]
            i+=1
        return strs[0][:i]