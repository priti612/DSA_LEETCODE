class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        p=strs[0]
        for i in strs[1:]:
            while not i.startswith(p):
                 p=p[:-1]
            if not p:
                return ""
        return p  