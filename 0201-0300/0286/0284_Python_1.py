import collections
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        def is_valid(x, y):
            return 0 <= x < s1 and 0 <= y < s2

        def get_near(x, y):
            res = []
            for xx, yy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if is_valid(xx, yy) and rooms[xx][yy] > 0:
                    res.append((xx, yy))
            return res

        if not rooms or not rooms[0]:
            return

        s1, s2 = len(rooms), len(rooms[0])

        doors = []
        for i1 in range(s1):
            for i2 in range(s2):
                if rooms[i1][i2] == 0:
                    doors.append((i1, i2))

        for door in doors:
            queue = collections.deque([door])
            while queue:
                (i1, i2) = queue.popleft()
                distance = rooms[i1][i2] + 1
                for (j1, j2) in get_near(i1, i2):
                    if rooms[j1][j2] > distance:
                        rooms[j1][j2] = distance
                        queue.append((j1, j2))


if __name__ == "__main__":
    #   3  -1   0   1
    #   2   2   1  -1
    #   1  -1   2  -1
    #   0  -1   3   4
    matrix = [
        [float("inf"), -1, 0, float("inf")],
        [float("inf"), float("inf"), float("inf"), -1],
        [float("inf"), -1, float("inf"), -1],
        [0, -1, float("inf"), float("inf")]
    ]
    Solution().wallsAndGates(matrix)
    print(matrix)
