from typing import List


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # [[0,1],[2,3,4,5]]
    print(Solution().findCriticalAndPseudoCriticalEdges(n=5,
                                                        edges=[[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3],
                                                               [3, 4, 3], [1, 4, 6]]))

    # [[],[0,1,2,3]]
    print(Solution().findCriticalAndPseudoCriticalEdges(n=4, edges=[[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]))
