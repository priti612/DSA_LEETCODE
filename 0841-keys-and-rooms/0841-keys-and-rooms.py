class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vis=set()
        def room(i):
            vis.add(i)
            for nei in rooms[i]:
                if nei not in vis:
                    room(nei)

        room(0)
        return len(rooms)==len(vis)