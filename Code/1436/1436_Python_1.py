from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        maybe = set()
        wrong = set()
        for path in paths:
            wrong.add(path[0])
            maybe.add(path[1])
        return (maybe - wrong).pop()


if __name__ == "__main__":
    print(
        Solution().destCity(paths=[["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))  # "Sao Paulo"
    print(Solution().destCity(paths=[["B", "C"], ["D", "B"], ["C", "A"]]))  # "A"
    print(Solution().destCity(paths=[["A", "Z"]]))  # "Z"
