from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """


if __name__ == "__main__":
    #   3  -1   0   1
    #   2   2   1  -1
    #   1  -1   2  -1
    #   0  -1   3   4
    matrix = [
        [float("inf"), -1, 0, float("inf")],
        [float("inf"), float("inf"), float("inf"), -1],
        [float("inf"), -1, float("inf"), -1],
        [0, -1, float("inf"), float("inf")]
    ]
    Solution().wallsAndGates(matrix)
    print(matrix)
