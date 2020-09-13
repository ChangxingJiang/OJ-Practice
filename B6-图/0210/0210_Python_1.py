from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    # [0,1]
    print(Solution().findOrder(2, [[1, 0]]))

    # [0,1,2,3] or [0,2,1,3]
    print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
