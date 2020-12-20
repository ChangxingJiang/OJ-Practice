from typing import List


class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pass


if __name__ == "__main__":
    # [False,True]
    print(Solution().checkIfPrerequisite(n=2, prerequisites=[[1, 0]], queries=[[0, 1], [1, 0]]))

    # [False,False]
    print(Solution().checkIfPrerequisite(n=2, prerequisites=[], queries=[[1, 0], [0, 1]]))

    # [True,True]
    print(Solution().checkIfPrerequisite(n=3, prerequisites=[[1, 2], [1, 0], [2, 0]],
                                         queries=[[1, 0], [1, 2]]))

    # [False,True]
    print(Solution().checkIfPrerequisite(n=3, prerequisites=[[1, 0], [2, 0]], queries=[[0, 1], [2, 0]]))

    # [True,False,True,False]
    print(Solution().checkIfPrerequisite(n=5, prerequisites=[[0, 1], [1, 2], [2, 3], [3, 4]],
                                         queries=[[0, 4], [4, 0], [1, 3], [3, 0]]))
