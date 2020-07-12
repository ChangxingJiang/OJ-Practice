from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().maximalRectangle([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]))  # 6
