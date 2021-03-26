from typing import List


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().leadsToDestination(n=3, edges=[[0, 1], [0, 2]], source=0, destination=2))  # False
    print(Solution().leadsToDestination(n=4, edges=[[0, 1], [0, 3], [1, 2], [2, 1]], source=0, destination=3))  # False
    print(Solution().leadsToDestination(n=4, edges=[[0, 1], [0, 2], [1, 3], [2, 3]], source=0, destination=3))  # True
    print(Solution().leadsToDestination(n=3, edges=[[0, 1], [1, 1], [1, 2]], source=0, destination=2))  # False
    print(Solution().leadsToDestination(n=2, edges=[[0, 1], [1, 1]], source=0, destination=1))  # False
