class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inc=[0]*(numCourses+1)
        gp=defaultdict(list)
        if not prerequisites:
            return True
        for x,y in prerequisites:
            gp[y].append(x)
            inc[x]+=1
        q=deque()
        for i in range(numCourses):
            if inc[i]==0:
                q.append(i)
        ct=0
        while q:
            ct+=1
            w=q.popleft()
            for n in gp[w]:
                inc[n]-=1
                if inc[n]==0: 
                    q.append(n)
        return ct==numCourses