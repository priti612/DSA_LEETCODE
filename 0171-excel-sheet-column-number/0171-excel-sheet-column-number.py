class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        res=0
        for ch in columnTitle:
            val=0
            i=0
            while i<26:
                if ch==chr(65+i):
                    val=i+1
                    break
                i+=1
            res=res*26+val
        return res