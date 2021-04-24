from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] in edges[1]:
            return edges[0][0]
        else:
            return edges[0][1]


if __name__ == "__main__":
    print(Solution().findCenter(edges=[[1, 2], [2, 3], [4, 2]]))  # 2
    print(Solution().findCenter(edges=[[1, 2], [5, 1], [1, 3], [1, 4]]))  # 1
