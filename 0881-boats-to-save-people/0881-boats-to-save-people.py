class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)
        low=0
        high=n-1
        ct=0
        people.sort()
        while low<=high:
            if people[low]+people[high]<=limit:
                low+=1
                
            
            high-=1
            ct+=1

        return ct