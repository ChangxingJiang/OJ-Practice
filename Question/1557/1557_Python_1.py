from typing import List


# O(E)
# 图、有向图

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        point = set([i for i in range(n)])

        for edge in edges:
            if edge[1] in point:
                point.remove(edge[1])

        return list(point)


if __name__ == "__main__":
    # [0,3]
    print(Solution().findSmallestSetOfVertices(n=6, edges=[[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]))

    # [0,2,3]
    print(Solution().findSmallestSetOfVertices(n=5, edges=[[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]))
