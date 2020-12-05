from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    # 6
    print(Solution().cutOffTree([
        [1, 2, 3],
        [0, 0, 4],
        [7, 6, 5]
    ]))

    # -1
    print(Solution().cutOffTree([
        [1, 2, 3],
        [0, 0, 0],
        [7, 6, 5]
    ]))

    # 6
    print(Solution().cutOffTree([
        [2, 3, 4],
        [0, 0, 5],
        [8, 7, 6]
    ]))
