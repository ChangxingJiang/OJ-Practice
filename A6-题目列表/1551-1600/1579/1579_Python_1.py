from typing import List


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    # 2
    print(Solution().maxNumEdgesToRemove(
        n=4,
        edges=[[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]))

    # 0
    print(Solution().maxNumEdgesToRemove(
        n=4,
        edges=[[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]))

    # -1
