from typing import List


class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # [[1,1],[2,0],[4,2],[3,3],[2,4]]
    print(Solution().outerTrees([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]))

    # [[1,2],[2,2],[4,2]]
    print(Solution().outerTrees([[1, 2], [2, 2], [4, 2]]))
