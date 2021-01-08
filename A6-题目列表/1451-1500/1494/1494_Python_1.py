from typing import List


class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minNumberOfSemesters(n=4, dependencies=[[2, 1], [3, 1], [1, 4]], k=2))  # 3
    print(Solution().minNumberOfSemesters(n=5, dependencies=[[2, 1], [3, 1], [4, 1], [1, 5]], k=2))  # 4
    print(Solution().minNumberOfSemesters(n=11, dependencies=[], k=2))  # 6
