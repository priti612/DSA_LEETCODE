class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans=[]
        mini=float('inf')
        arr.sort()
        for i in range(len(arr)-1):
            
            mini=min(mini,arr[i+1]-arr[i])
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==mini:
                ans.append([arr[i],arr[i+1]])
        return ans