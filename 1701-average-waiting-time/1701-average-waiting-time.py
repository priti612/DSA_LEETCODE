class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        ans=0
        curr=0
        for i in range(len(customers)):
            arr=customers[i][0]
            time=customers[i][1]
            
            curr=max(curr,arr)+time
            
            ans+=curr-arr
            
        return (ans/len(customers))