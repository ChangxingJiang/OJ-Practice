from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        pass


if __name__ == "__main__":
    # True
    print(Solution().validWordSquare([
        "abcd",
        "bnrt",
        "crmy",
        "dtye"
    ]))

    # True
    print(Solution().validWordSquare([
        "abcd",
        "bnrt",
        "crm",
        "dt"
    ]))

    # False
    print(Solution().validWordSquare([
        "ball",
        "area",
        "read",
        "lady"
    ]))
