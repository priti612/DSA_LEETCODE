class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        
        # subarr=[]
        # f={}
        # ans=[]
        # if len(arr)==1:
        #     return 1
        # for i in range(len(arr)):
        #     for j in range(i,len(arr)):
        #         subarr.append((arr[i:j+1]))
        #         print(subarr)
        # for sub in subarr:
        #     res=0
        #     for sb in sub:
        #         res|=sb
        #         ans.append(res)
        # return len(set(ans))
        ans=set()
        curr=set()
        for x in arr:
            curr={x | y for y in curr}|{x}
            ans|=curr
        return len(ans)
        