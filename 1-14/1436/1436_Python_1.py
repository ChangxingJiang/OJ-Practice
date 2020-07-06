from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        pass


if __name__ == "__main__":
    print(
        Solution().destCity(paths=[["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))  # "Sao Paulo"
    print(Solution().destCity(paths=[["B", "C"], ["D", "B"], ["C", "A"]]))  # "A"
    print(Solution().destCity(paths=[["A", "Z"]]))  # "Z"
