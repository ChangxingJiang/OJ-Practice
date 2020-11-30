from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    # 2
    print(Solution().countComponents(n=5, edges=[[0, 1], [1, 2], [3, 4]]))

    # 1
    print(Solution().countComponents(n=5, edges=[[0, 1], [1, 2], [2, 3], [3, 4]]))
