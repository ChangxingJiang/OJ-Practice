import collections
from typing import List


class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        def is_valid(x, y):
            return 0 <= x < s1 and 0 <= y < s2

        def get_near(x, y):
            res = []
            for xx, yy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if is_valid(xx, yy):
                    res.append((xx, yy))
            return res

        s1, s2 = len(image), len(image[0])

        min_x, min_y, max_x, max_y = x, y, x, y
        visited = set()
        queue = collections.deque([(x, y)])
        while queue:
            x1, y1 = queue.popleft()
            for x2, y2 in get_near(x1, y1):
                if image[x2][y2] == "1" and (x2, y2) not in visited:
                    visited.add((x2, y2))
                    queue.append((x2, y2))
                    min_x, max_x = min(min_x, x2), max(max_x, x2)
                    min_y, max_y = min(min_y, y2), max(max_y, y2)

        return (max_x - min_x + 1) * (max_y - min_y + 1)


if __name__ == "__main__":
    # 6
    print(Solution().minArea(
        image=[
            ["0", "0", "1", "0"],
            ["0", "1", "1", "0"],
            ["0", "1", "0", "0"]
        ],
        x=0, y=2
    ))
