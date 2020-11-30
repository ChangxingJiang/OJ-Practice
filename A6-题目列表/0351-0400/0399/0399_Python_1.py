from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        pass


if __name__ == "__main__":
    # [6.0, 0.5, -1.0, 1.0, -1.0 ]
    print(Solution().calcEquation(
        equations=[["a", "b"], ["b", "c"]],
        values=[2.0, 3.0],
        queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    ))
