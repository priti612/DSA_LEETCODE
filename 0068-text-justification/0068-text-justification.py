class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res=[]
        line=[]
        l=0
        for w in words:
            if l+len(w)+len(line)>maxWidth:
                sp=maxWidth-l
                gp=len(line)-1

                if gp==0:
                    res.append(line[0]+' '*sp)
                else:
                    s=sp//gp
                    extra=sp%gp
                    for i in range(extra):
                        line[i]+=' '
                    res.append((' '*s).join(line))
                line=[]
                l=0
            line.append(w)
            l+=len(w)
        last=' '.join(line)
        last+=' '*(maxWidth-len(last))
        res.append(last)
        return res
