from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # [[1,3]]
    print(Solution().criticalConnections(n=4, connections=[[0, 1], [1, 2], [2, 0], [1, 3]]))
