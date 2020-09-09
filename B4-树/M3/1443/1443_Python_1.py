from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        pass


if __name__ == "__main__":
    # 8
    print(Solution().minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], hasApple=[False, False, True, False, True, True, False]))

    # 6
    print(Solution().minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], hasApple=[False, False, True, False, False, True, False]))

    # 0
    print(Solution().minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], hasApple=[False, False, False, False, False, False, False]))
