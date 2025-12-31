class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res=""
        while columnNumber>0:
            columnNumber-=1
            val=columnNumber%26
            res=chr(65+val)+res
            columnNumber//=26
        return res
