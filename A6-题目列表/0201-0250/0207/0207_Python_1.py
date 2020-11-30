from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().canFinish(2, [[1, 0]]))  # True
    print(Solution().canFinish(2, [[1, 0], [0, 1]]))  # False
