class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res=list(zip(names,heights))
        print(res)
        res.sort(key=lambda x:x[1],reverse=True)
        return [p[0] for p in res]