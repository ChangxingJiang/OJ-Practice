import collections
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        queue = collections.deque([0])
        while queue:
            n1 = queue.popleft()
            for n2 in rooms[n1]:
                if n2 not in visited:
                    visited.add(n2)
                    queue.append(n2)
        return len(visited) == len(rooms)


if __name__ == "__main__":
    print(Solution().canVisitAllRooms([[1], [2], [3], []]))  # True
    print(Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))  # False
