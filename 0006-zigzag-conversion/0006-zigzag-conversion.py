class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans=[]
        if numRows==1:
            return s
        for i in range(numRows):
            idx=i
            niche=2*(numRows-1-i) # jb hm niche jate hai upar aate same row k liye
            upar=2*i # jb hm rupar se niche aate hai
            found=True
            while idx<len(s):
                ans.append(s[idx])
                if i==0:
                    idx+=niche
                elif i==(numRows-1):
                    idx+=upar
                else:
                    if found:
                        idx+=niche
                    else:
                        idx+=upar
                    found =not found

        return "".join(ans)

