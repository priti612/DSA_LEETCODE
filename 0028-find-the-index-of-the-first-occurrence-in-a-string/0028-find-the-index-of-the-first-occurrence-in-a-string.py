class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        
        """
        # pre=needle[0]
        # for s in haystack:
        #     while not s.startswith(pre):
        #         return -1
        # return 0
        return haystack.find(needle)