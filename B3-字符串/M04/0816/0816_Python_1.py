from typing import List


class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        pass


if __name__ == "__main__":
    print(Solution().ambiguousCoordinates("(123)"))  # ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
    print(Solution().ambiguousCoordinates("(00011)"))  # ["(0.001, 1)", "(0, 0.011)"]
    print(Solution().ambiguousCoordinates("(0123)"))  # ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
    print(Solution().ambiguousCoordinates("(100)"))  # [(10, 0)]
