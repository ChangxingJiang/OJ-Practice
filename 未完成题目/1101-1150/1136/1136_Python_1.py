from typing import List


class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minimumSemesters(N=3, relations=[[1, 3], [2, 3]]))  # 2
    print(Solution().minimumSemesters(N=3, relations=[[1, 2], [2, 3], [3, 1]]))  # -1
